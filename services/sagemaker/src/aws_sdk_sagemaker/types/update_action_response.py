"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.action_arn


class UpdateActionResponse(TypedDict, closed=True):
    action_arn: NotRequired["aws_sdk_sagemaker.types.action_arn.ActionArn"]
    """<p>The Amazon Resource Name (ARN) of the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateActionResponse) -> dict:
    out: dict = {}
    if "action_arn" in value:
        out["ActionArn"] = value["action_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateActionResponse:
    out: UpdateActionResponse = {}  # type: ignore[typeddict-item]
    if "ActionArn" in data:
        out["action_arn"] = data["ActionArn"]
    return out
