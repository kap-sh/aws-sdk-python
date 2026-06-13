"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ExclusionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

ExclusionStatus: TypeAlias = Literal[
    "excluded",
    "included",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "excluded",
        "included",
    )
)


def serialize_json(value: ExclusionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExclusionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExclusionStatus value: {data!r}")
    return cast(ExclusionStatus, data)
