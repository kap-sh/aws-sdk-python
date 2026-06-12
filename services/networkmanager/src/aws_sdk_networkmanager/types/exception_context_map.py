"""Generated from Smithy shape ``com.amazonaws.networkmanager#ExceptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.exception_context_key
    import aws_sdk_networkmanager.types.exception_context_value

ExceptionContextMap: TypeAlias = dict[
    "aws_sdk_networkmanager.types.exception_context_key.ExceptionContextKey",
    "aws_sdk_networkmanager.types.exception_context_value.ExceptionContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExceptionContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExceptionContextMap:
    out: ExceptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
