"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateActionTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class UpdateActionTargetRequest(TypedDict):
    action_target_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the custom action target to update.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The updated name of the custom action target.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The updated description for the custom action target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionTargetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateActionTargetRequest:
    out: UpdateActionTargetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
