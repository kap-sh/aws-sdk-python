"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

StopCisSessionStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "INTERRUPTED",
    "UNSUPPORTED_OS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
        "INTERRUPTED",
        "UNSUPPORTED_OS",
    )
)


def serialize_json(value: StopCisSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> StopCisSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StopCisSessionStatus value: {data!r}")
    return cast(StopCisSessionStatus, data)
