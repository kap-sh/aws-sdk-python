"""Generated from Smithy shape ``com.amazonaws.iot#DomainConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

DomainConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainConfigurationStatus:
    return cast(DomainConfigurationStatus, data)
