"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableWarmThroughputDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.table_status


class TableWarmThroughputDescription(TypedDict):
    read_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in read units per second.</p>"""
    write_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in write units per second.</p>"""
    status: NotRequired["aws_sdk_dynamodb.types.table_status.TableStatus"]
    """<p>Represents warm throughput value of the base table.</p>"""
