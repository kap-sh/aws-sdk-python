"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

OTAUpdateStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: OTAUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> OTAUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OTAUpdateStatus value: {data!r}")
    return cast(OTAUpdateStatus, data)
