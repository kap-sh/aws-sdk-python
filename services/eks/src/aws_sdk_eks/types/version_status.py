"""Generated from Smithy shape ``com.amazonaws.eks#VersionStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

VersionStatus: TypeAlias = Literal[
    "UNSUPPORTED",
    "STANDARD_SUPPORT",
    "EXTENDED_SUPPORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNSUPPORTED",
        "STANDARD_SUPPORT",
        "EXTENDED_SUPPORT",
    )
)


def serialize_json(value: VersionStatus) -> str:
    return value


def deserialize_json(data: str) -> VersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VersionStatus value: {data!r}")
    return cast(VersionStatus, data)
