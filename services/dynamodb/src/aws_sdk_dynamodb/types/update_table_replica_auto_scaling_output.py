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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableReplicaAutoScalingOutput) -> dict:
    out: dict = {}
    if "table_auto_scaling_description" in value:
        import aws_sdk_dynamodb.types.table_auto_scaling_description

        out["TableAutoScalingDescription"] = (
            aws_sdk_dynamodb.types.table_auto_scaling_description.serialize_aws_json_1_0(
                value["table_auto_scaling_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableReplicaAutoScalingOutput:
    out: UpdateTableReplicaAutoScalingOutput = {}  # type: ignore[typeddict-item]
    if "TableAutoScalingDescription" in data:
        import aws_sdk_dynamodb.types.table_auto_scaling_description

        out["table_auto_scaling_description"] = (
            aws_sdk_dynamodb.types.table_auto_scaling_description.deserialize_aws_json_1_0(
                data["TableAutoScalingDescription"]
            )
        )
    return out
