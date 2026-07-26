"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfKeyValuePair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.key_value_pair

__listOfKeyValuePair: TypeAlias = list["capo_macie2.types.key_value_pair.KeyValuePair"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKeyValuePair) -> list:
    import capo_macie2.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_macie2.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKeyValuePair:
    import capo_macie2.types.key_value_pair

    out: __listOfKeyValuePair = []
    for item in data:
        out.append(capo_macie2.types.key_value_pair.deserialize_json(item))
    return out
