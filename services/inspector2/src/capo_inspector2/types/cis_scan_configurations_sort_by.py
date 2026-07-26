"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfigurationsSortBy``."""

from typing import Literal, TypeAlias, cast

CisScanConfigurationsSortBy: TypeAlias = Literal[
    "SCAN_NAME",
    "SCAN_CONFIGURATION_ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanConfigurationsSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanConfigurationsSortBy:
    return cast(CisScanConfigurationsSortBy, data)
