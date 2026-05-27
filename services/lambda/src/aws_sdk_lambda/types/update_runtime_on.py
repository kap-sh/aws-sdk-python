"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateRuntimeOn``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

UpdateRuntimeOn: TypeAlias = Literal[
    "Auto",
    "Manual",
    "FunctionUpdate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Auto",
        "Manual",
        "FunctionUpdate",
    )
)


def serialize_json(value: UpdateRuntimeOn) -> str:
    return value


def deserialize_json(data: str) -> UpdateRuntimeOn:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateRuntimeOn value: {data!r}")
    return cast(UpdateRuntimeOn, data)
