"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.action_arn


class DeleteActionResponse(TypedDict, closed=True):
    action_arn: NotRequired["capo_sagemaker.types.action_arn.ActionArn"]
    """<p>The Amazon Resource Name (ARN) of the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteActionResponse) -> dict:
    out: dict = {}
    if "action_arn" in value:
        out["ActionArn"] = value["action_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteActionResponse:
    out: DeleteActionResponse = {}  # type: ignore[typeddict-item]
    if "ActionArn" in data:
        out["action_arn"] = data["ActionArn"]
    return out
