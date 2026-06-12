"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfTagValuePair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.tag_value_pair

__listOfTagValuePair: TypeAlias = list[
    "aws_sdk_macie2.types.tag_value_pair.TagValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTagValuePair) -> list:
    import aws_sdk_macie2.types.tag_value_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.tag_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTagValuePair:
    import aws_sdk_macie2.types.tag_value_pair

    out: __listOfTagValuePair = []
    for item in data:
        out.append(aws_sdk_macie2.types.tag_value_pair.deserialize_json(item))
    return out
