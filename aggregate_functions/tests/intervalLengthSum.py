from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_IntervalLengthSum,
)

from helpers.common import check_clickhouse_version
from aggregate_functions.tests.steps import get_snapshot_id
from aggregate_functions.tests.deltaSumTimestamp import feature as checks


@TestFeature
@Name("intervalLengthSum")
@Requirements(
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_IntervalLengthSum("1.0")
)
def feature(self, func="intervalLengthSum({params})", table=None):
    """Check intervalLengthSum aggregate function by using the same tests as for deltaSumTimestamp."""
    clickhouse_version = (
        "<22.4" if check_clickhouse_version("<23.2")(self) else ">=23.2"
    )
    self.context.snapshot_id = get_snapshot_id(clickhouse_version=clickhouse_version)

    if table is None:
        table = self.context.table

    checks(
        func=func,
        table=table,
        both_arguments_with_the_same_datatype=True,
        snapshot_id=self.context.snapshot_id,
    )
