"""Generated from Smithy shape ``com.amazonaws.ecs#AutoRepairConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_actions_status


class AutoRepairConfiguration(TypedDict):
    actions_status: NotRequired[
        "aws_sdk_ecs.types.auto_repair_actions_status.AutoRepairActionsStatus"
    ]
    """<p>The status of auto repair actions for the capacity provider. When set to <code>ENABLED</code>, Amazon ECS automatically replaces container instances with an <code>IMPAIRED</code> health status. When set to <code>DISABLED</code>, Amazon ECS still monitors container instance health but does not automatically replace impaired instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRepairConfiguration) -> dict:
    out: dict = {}
    if "actions_status" in value:
        import aws_sdk_ecs.types.auto_repair_actions_status

        out["actionsStatus"] = (
            aws_sdk_ecs.types.auto_repair_actions_status.serialize_aws_json_1_1(
                value["actions_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoRepairConfiguration:
    out: AutoRepairConfiguration = {}  # type: ignore[typeddict-item]
    if "actionsStatus" in data:
        import aws_sdk_ecs.types.auto_repair_actions_status

        out["actions_status"] = (
            aws_sdk_ecs.types.auto_repair_actions_status.deserialize_aws_json_1_1(
                data["actionsStatus"]
            )
        )
    return out
