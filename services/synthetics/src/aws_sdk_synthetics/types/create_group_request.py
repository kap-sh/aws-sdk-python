"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group_name
    import aws_sdk_synthetics.types.tag_map


class CreateGroupRequest(TypedDict):
    name: "aws_sdk_synthetics.types.group_name.GroupName"
    """<p>The name for the group. It can include any Unicode characters.</p> <p>The names for all groups in your account, across all Regions, must be unique.</p>"""
    tags: NotRequired["aws_sdk_synthetics.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to associate with the group. You can associate as many as 50 tags with a group.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_synthetics.types.tag_map

        out["Tags"] = aws_sdk_synthetics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateGroupRequest.name required")
    if "Tags" in data:
        import aws_sdk_synthetics.types.tag_map

        out["tags"] = aws_sdk_synthetics.types.tag_map.deserialize_json(data["Tags"])
    return out
