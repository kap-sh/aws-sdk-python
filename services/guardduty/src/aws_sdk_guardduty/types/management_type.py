"""Generated from Smithy shape ``com.amazonaws.guardduty#ManagementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ManagementType: TypeAlias = Literal[
    "AUTO_MANAGED",
    "MANUAL",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_MANAGED",
        "MANUAL",
        "DISABLED",
    )
)


def serialize_json(value: ManagementType) -> str:
    return value


def deserialize_json(data: str) -> ManagementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagementType value: {data!r}")
    return cast(ManagementType, data)
