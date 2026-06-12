"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceResolutionStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourceResolutionStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: ResourceResolutionStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourceResolutionStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceResolutionStatusType value: {data!r}"
        )
    return cast(ResourceResolutionStatusType, data)
