"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.session_tag

SessionTagList: TypeAlias = list["aws_sdk_quicksight.types.session_tag.SessionTag"]


# --- restJson1 ser/de ---
def serialize_json(value: SessionTagList) -> list:
    import aws_sdk_quicksight.types.session_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.session_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionTagList:
    import aws_sdk_quicksight.types.session_tag

    out: SessionTagList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.session_tag.deserialize_json(item))
    return out
