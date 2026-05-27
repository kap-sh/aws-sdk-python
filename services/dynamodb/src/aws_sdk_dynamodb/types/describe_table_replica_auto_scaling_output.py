"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTableReplicaAutoScalingOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_auto_scaling_description


class DescribeTableReplicaAutoScalingOutput(TypedDict):
    table_auto_scaling_description: NotRequired[
        "aws_sdk_dynamodb.types.table_auto_scaling_description.TableAutoScalingDescription"
    ]
    """<p>Represents the auto scaling properties of the table.</p>"""
