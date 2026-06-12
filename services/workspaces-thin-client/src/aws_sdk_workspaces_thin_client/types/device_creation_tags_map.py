"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceCreationTagsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.device_creation_tag_key
    import aws_sdk_workspaces_thin_client.types.device_creation_tag_value

DeviceCreationTagsMap: TypeAlias = dict[
    "aws_sdk_workspaces_thin_client.types.device_creation_tag_key.DeviceCreationTagKey",
    "aws_sdk_workspaces_thin_client.types.device_creation_tag_value.DeviceCreationTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DeviceCreationTagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DeviceCreationTagsMap:
    out: DeviceCreationTagsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
