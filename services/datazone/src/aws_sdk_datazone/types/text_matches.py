"""Generated from Smithy shape ``com.amazonaws.datazone#TextMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.text_match_item

TextMatches: TypeAlias = list["aws_sdk_datazone.types.text_match_item.TextMatchItem"]


# --- restJson1 ser/de ---
def serialize_json(value: TextMatches) -> list:
    import aws_sdk_datazone.types.text_match_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.text_match_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextMatches:
    import aws_sdk_datazone.types.text_match_item

    out: TextMatches = []
    for item in data:
        out.append(aws_sdk_datazone.types.text_match_item.deserialize_json(item))
    return out
