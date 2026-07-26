"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckOperationListingMode``."""

from typing import Literal, TypeAlias, cast

ConfigurationCheckOperationListingMode: TypeAlias = Literal[
    "ALL_OPERATIONS",
    "LATEST_PER_CHECK",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckOperationListingMode) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationCheckOperationListingMode:
    return cast(ConfigurationCheckOperationListingMode, data)
