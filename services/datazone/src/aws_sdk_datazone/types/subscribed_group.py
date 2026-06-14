"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_profile_id
    import aws_sdk_datazone.types.group_profile_name


class SubscribedGroup(TypedDict):
    id: NotRequired["aws_sdk_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The ID of the subscribed group.</p>"""
    name: NotRequired["aws_sdk_datazone.types.group_profile_name.GroupProfileName"]
    """<p>The name of the subscribed group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SubscribedGroup:
    out: SubscribedGroup = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
