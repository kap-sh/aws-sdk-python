"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OrganizationConfigurationStatus: TypeAlias = Literal[
    "PENDING",
    "ENABLED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ENABLED",
        "FAILED",
    )
)


def serialize_json(value: OrganizationConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> OrganizationConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationConfigurationStatus value: {data!r}"
        )
    return cast(OrganizationConfigurationStatus, data)
