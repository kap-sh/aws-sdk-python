"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "ok",
    "warning",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "warning",
        "error",
    )
)


def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
