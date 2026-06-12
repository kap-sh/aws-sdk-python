"""Generated from Smithy shape ``com.amazonaws.batch#PlatformCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.platform_capability

PlatformCapabilityList: TypeAlias = list[
    "aws_sdk_batch.types.platform_capability.PlatformCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlatformCapabilityList) -> list:
    import aws_sdk_batch.types.platform_capability

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.platform_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlatformCapabilityList:
    import aws_sdk_batch.types.platform_capability

    out: PlatformCapabilityList = []
    for item in data:
        out.append(aws_sdk_batch.types.platform_capability.deserialize_json(item))
    return out
