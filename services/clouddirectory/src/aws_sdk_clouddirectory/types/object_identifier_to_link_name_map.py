"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectIdentifierToLinkNameMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_identifier

ObjectIdentifierToLinkNameMap: TypeAlias = dict[
    "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier",
    "aws_sdk_clouddirectory.types.link_name.LinkName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ObjectIdentifierToLinkNameMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ObjectIdentifierToLinkNameMap:
    out: ObjectIdentifierToLinkNameMap = {}
    for key, value in data.items():
        out[key] = value
    return out
