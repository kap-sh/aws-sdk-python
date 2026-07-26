"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfTagValuePair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.tag_value_pair

__listOfTagValuePair: TypeAlias = list["capo_macie2.types.tag_value_pair.TagValuePair"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTagValuePair) -> list:
    import capo_macie2.types.tag_value_pair

    out: list = []
    for item in value:
        out.append(capo_macie2.types.tag_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTagValuePair:
    import capo_macie2.types.tag_value_pair

    out: __listOfTagValuePair = []
    for item in data:
        out.append(capo_macie2.types.tag_value_pair.deserialize_json(item))
    return out
