"""Generated from Smithy shape ``com.amazonaws.connect#TagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_set

TagsList: TypeAlias = list["aws_sdk_connect.types.tag_set.TagSet"]


# --- restJson1 ser/de ---
def serialize_json(value: TagsList) -> list:
    import aws_sdk_connect.types.tag_set

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.tag_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagsList:
    import aws_sdk_connect.types.tag_set

    out: TagsList = []
    for item in data:
        out.append(aws_sdk_connect.types.tag_set.deserialize_json(item))
    return out
