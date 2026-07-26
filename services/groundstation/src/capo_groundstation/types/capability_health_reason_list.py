"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealthReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.capability_health_reason

CapabilityHealthReasonList: TypeAlias = list[
    "capo_groundstation.types.capability_health_reason.CapabilityHealthReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityHealthReasonList) -> list:
    import capo_groundstation.types.capability_health_reason

    out: list = []
    for item in value:
        out.append(
            capo_groundstation.types.capability_health_reason.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapabilityHealthReasonList:
    import capo_groundstation.types.capability_health_reason

    out: CapabilityHealthReasonList = []
    for item in data:
        out.append(
            capo_groundstation.types.capability_health_reason.deserialize_json(item)
        )
    return out
