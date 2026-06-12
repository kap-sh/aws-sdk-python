"""Generated from Smithy shape ``com.amazonaws.amplify#BuildComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

BuildComputeType: TypeAlias = Literal[
    "STANDARD_8GB",
    "LARGE_16GB",
    "XLARGE_72GB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD_8GB",
        "LARGE_16GB",
        "XLARGE_72GB",
    )
)


def serialize_json(value: BuildComputeType) -> str:
    return value


def deserialize_json(data: str) -> BuildComputeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuildComputeType value: {data!r}")
    return cast(BuildComputeType, data)
