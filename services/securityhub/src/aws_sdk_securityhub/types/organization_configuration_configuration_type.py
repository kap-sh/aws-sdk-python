"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationConfigurationConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OrganizationConfigurationConfigurationType: TypeAlias = Literal[
    "CENTRAL",
    "LOCAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENTRAL",
        "LOCAL",
    )
)


def serialize_json(value: OrganizationConfigurationConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> OrganizationConfigurationConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationConfigurationConfigurationType value: {data!r}"
        )
    return cast(OrganizationConfigurationConfigurationType, data)
