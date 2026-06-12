"""Generated from Smithy shape ``com.amazonaws.iot#MissingContextValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.missing_context_value

MissingContextValues: TypeAlias = list[
    "aws_sdk_iot.types.missing_context_value.MissingContextValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MissingContextValues) -> list:
    return list(value)


def deserialize_json(data: list) -> MissingContextValues:
    return list(data)
