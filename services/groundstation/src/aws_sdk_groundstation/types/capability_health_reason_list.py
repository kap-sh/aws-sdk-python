"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealthReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.capability_health_reason

CapabilityHealthReasonList: TypeAlias = list[
    "aws_sdk_groundstation.types.capability_health_reason.CapabilityHealthReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityHealthReasonList) -> list:
    import aws_sdk_groundstation.types.capability_health_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.capability_health_reason.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapabilityHealthReasonList:
    import aws_sdk_groundstation.types.capability_health_reason

    out: CapabilityHealthReasonList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.capability_health_reason.deserialize_json(item)
        )
    return out
