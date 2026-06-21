"""Generated from Smithy shape ``com.amazonaws.synthetics#ProvisionedResourceCleanupSetting``."""

from typing import Literal, TypeAlias, cast

ProvisionedResourceCleanupSetting: TypeAlias = Literal[
    "AUTOMATIC",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedResourceCleanupSetting) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedResourceCleanupSetting:
    return cast(ProvisionedResourceCleanupSetting, data)
