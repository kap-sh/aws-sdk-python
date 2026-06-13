"""Generated from Smithy shape ``com.amazonaws.groundstation#VersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

VersionStatus: TypeAlias = Literal[
    "UPDATING",
    "ACTIVE",
    "SUPERSEDED",
    "FAILED_TO_UPDATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "ACTIVE",
        "SUPERSEDED",
        "FAILED_TO_UPDATE",
    )
)


def serialize_json(value: VersionStatus) -> str:
    return value


def deserialize_json(data: str) -> VersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VersionStatus value: {data!r}")
    return cast(VersionStatus, data)
