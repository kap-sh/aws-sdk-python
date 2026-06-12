"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfKeyValuePair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.key_value_pair

__listOfKeyValuePair: TypeAlias = list[
    "aws_sdk_macie2.types.key_value_pair.KeyValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKeyValuePair) -> list:
    import aws_sdk_macie2.types.key_value_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKeyValuePair:
    import aws_sdk_macie2.types.key_value_pair

    out: __listOfKeyValuePair = []
    for item in data:
        out.append(aws_sdk_macie2.types.key_value_pair.deserialize_json(item))
    return out
