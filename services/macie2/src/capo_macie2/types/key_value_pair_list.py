"""Generated from Smithy shape ``com.amazonaws.macie2#KeyValuePairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.key_value_pair

KeyValuePairList: TypeAlias = list["capo_macie2.types.key_value_pair.KeyValuePair"]


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuePairList) -> list:
    import capo_macie2.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_macie2.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> KeyValuePairList:
    import capo_macie2.types.key_value_pair

    out: KeyValuePairList = []
    for item in data:
        out.append(capo_macie2.types.key_value_pair.deserialize_json(item))
    return out
