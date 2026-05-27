"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexWarmThroughputDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_status
    import aws_sdk_dynamodb.types.positive_long_object


class GlobalSecondaryIndexWarmThroughputDescription(TypedDict):
    read_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents warm throughput read units per second value for a global secondary index.</p>"""
    write_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents warm throughput write units per second value for a global secondary index.</p>"""
    status: NotRequired["aws_sdk_dynamodb.types.index_status.IndexStatus"]
    """<p>Represents the warm throughput status being created or updated on a global secondary index. The status can only be <code>UPDATING</code> or <code>ACTIVE</code>.</p>"""
