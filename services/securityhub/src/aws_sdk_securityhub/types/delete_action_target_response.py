"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteActionTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DeleteActionTargetResponse(TypedDict):
    action_target_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the custom action target that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteActionTargetResponse) -> dict:
    out: dict = {}
    if "action_target_arn" in value:
        out["ActionTargetArn"] = value["action_target_arn"]
    return out


def deserialize_json(data: dict) -> DeleteActionTargetResponse:
    out: DeleteActionTargetResponse = {}  # type: ignore[typeddict-item]
    if "ActionTargetArn" in data:
        out["action_target_arn"] = data["ActionTargetArn"]
    return out
