"""Generated from Smithy shape ``com.amazonaws.qapps#InputCardComputeMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

InputCardComputeMode: TypeAlias = Literal[
    "append",
    "replace",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "append",
        "replace",
    )
)


def serialize_json(value: InputCardComputeMode) -> str:
    return value


def deserialize_json(data: str) -> InputCardComputeMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputCardComputeMode value: {data!r}")
    return cast(InputCardComputeMode, data)
