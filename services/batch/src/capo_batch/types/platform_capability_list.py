"""Generated from Smithy shape ``com.amazonaws.batch#PlatformCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.platform_capability

PlatformCapabilityList: TypeAlias = list[
    "capo_batch.types.platform_capability.PlatformCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlatformCapabilityList) -> list:
    import capo_batch.types.platform_capability

    out: list = []
    for item in value:
        out.append(capo_batch.types.platform_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlatformCapabilityList:
    import capo_batch.types.platform_capability

    out: PlatformCapabilityList = []
    for item in data:
        out.append(capo_batch.types.platform_capability.deserialize_json(item))
    return out
