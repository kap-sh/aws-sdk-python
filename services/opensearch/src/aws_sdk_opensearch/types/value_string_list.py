"""Generated from Smithy shape ``com.amazonaws.opensearch#ValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.non_empty_string

ValueStringList: TypeAlias = list[
    "aws_sdk_opensearch.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueStringList:
    return list(data)
