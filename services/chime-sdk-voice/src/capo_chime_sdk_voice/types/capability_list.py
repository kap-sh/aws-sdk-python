"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.capability

CapabilityList: TypeAlias = list["capo_chime_sdk_voice.types.capability.Capability"]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityList) -> list:
    import capo_chime_sdk_voice.types.capability

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilityList:
    import capo_chime_sdk_voice.types.capability

    out: CapabilityList = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.capability.deserialize_json(item))
    return out
