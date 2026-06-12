"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEventContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.string


class DeployTargetEventContext(TypedDict):
    ssm_command_id: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The command ID for the event for the deploy action.</p>"""
    message: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The context message for the event for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEventContext) -> dict:
    out: dict = {}
    if "ssm_command_id" in value:
        out["ssmCommandId"] = value["ssm_command_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployTargetEventContext:
    out: DeployTargetEventContext = {}  # type: ignore[typeddict-item]
    if "ssmCommandId" in data:
        out["ssm_command_id"] = data["ssmCommandId"]
    if "message" in data:
        out["message"] = data["message"]
    return out
