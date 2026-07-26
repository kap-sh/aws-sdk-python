"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateActionTargetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class CreateActionTargetResponse(TypedDict, closed=True):
    action_target_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) for the custom action target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActionTargetResponse) -> dict:
    out: dict = {}
    if "action_target_arn" in value:
        out["ActionTargetArn"] = value["action_target_arn"]
    return out


def deserialize_json(data: dict) -> CreateActionTargetResponse:
    out: CreateActionTargetResponse = {}  # type: ignore[typeddict-item]
    if "ActionTargetArn" in data:
        out["action_target_arn"] = data["ActionTargetArn"]
    return out
