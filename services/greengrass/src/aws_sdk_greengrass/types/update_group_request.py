"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateGroupRequest(TypedDict, closed=True):
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the definition."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
