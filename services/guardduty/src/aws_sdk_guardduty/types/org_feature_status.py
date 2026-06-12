"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeatureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

OrgFeatureStatus: TypeAlias = Literal[
    "NEW",
    "NONE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "NONE",
        "ALL",
    )
)


def serialize_json(value: OrgFeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> OrgFeatureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrgFeatureStatus value: {data!r}")
    return cast(OrgFeatureStatus, data)
