"""Generated from Smithy shape ``com.amazonaws.macie2#KeyValuePairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.key_value_pair

KeyValuePairList: TypeAlias = list["aws_sdk_macie2.types.key_value_pair.KeyValuePair"]


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuePairList) -> list:
    import aws_sdk_macie2.types.key_value_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> KeyValuePairList:
    import aws_sdk_macie2.types.key_value_pair

    out: KeyValuePairList = []
    for item in data:
        out.append(aws_sdk_macie2.types.key_value_pair.deserialize_json(item))
    return out
