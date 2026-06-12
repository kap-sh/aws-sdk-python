"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier

ObjectIdentifierList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectIdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> ObjectIdentifierList:
    return list(data)
