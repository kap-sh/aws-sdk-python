"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ObjectPrefixes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.object_prefix

ObjectPrefixes: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.object_prefix.ObjectPrefix"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectPrefixes) -> list:
    return list(value)


def deserialize_json(data: list) -> ObjectPrefixes:
    return list(data)
