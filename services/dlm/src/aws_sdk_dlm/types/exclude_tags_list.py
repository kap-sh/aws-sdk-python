"""Generated from Smithy shape ``com.amazonaws.dlm#ExcludeTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.tag

ExcludeTagsList: TypeAlias = list["aws_sdk_dlm.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludeTagsList) -> list:
    import aws_sdk_dlm.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExcludeTagsList:
    import aws_sdk_dlm.types.tag

    out: ExcludeTagsList = []
    for item in data:
        out.append(aws_sdk_dlm.types.tag.deserialize_json(item))
    return out
