"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationConfigurationConfigurationType``."""

from typing import Literal, TypeAlias, cast

OrganizationConfigurationConfigurationType: TypeAlias = Literal[
    "CENTRAL",
    "LOCAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationConfigurationConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> OrganizationConfigurationConfigurationType:
    return cast(OrganizationConfigurationConfigurationType, data)
