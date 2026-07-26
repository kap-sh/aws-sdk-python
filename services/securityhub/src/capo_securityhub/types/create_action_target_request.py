"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateActionTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class CreateActionTargetRequest(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the custom action target. Can contain up to 20 characters.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description for the custom action target.</p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID for the custom action target. Can contain up to 20 alphanumeric characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActionTargetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateActionTargetRequest:
    out: CreateActionTargetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
