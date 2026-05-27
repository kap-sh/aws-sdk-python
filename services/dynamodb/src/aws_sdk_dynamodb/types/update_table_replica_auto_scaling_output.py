"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableReplicaAutoScalingOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_auto_scaling_description


class UpdateTableReplicaAutoScalingOutput(TypedDict):
    table_auto_scaling_description: NotRequired[
        "aws_sdk_dynamodb.types.table_auto_scaling_description.TableAutoScalingDescription"
    ]
    """<p>Returns information about the auto scaling settings of a table with replicas.</p>"""
