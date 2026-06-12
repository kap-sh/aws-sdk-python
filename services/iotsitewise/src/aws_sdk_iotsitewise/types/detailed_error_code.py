"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

DetailedErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_COMPUTE_LOCATION",
    "INCOMPATIBLE_FORWARDING_CONFIGURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCOMPATIBLE_COMPUTE_LOCATION",
        "INCOMPATIBLE_FORWARDING_CONFIGURATION",
    )
)


def serialize_json(value: DetailedErrorCode) -> str:
    return value


def deserialize_json(data: str) -> DetailedErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailedErrorCode value: {data!r}")
    return cast(DetailedErrorCode, data)
