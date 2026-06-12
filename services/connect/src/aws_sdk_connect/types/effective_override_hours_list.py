"""Generated from Smithy shape ``com.amazonaws.connect#EffectiveOverrideHoursList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.effective_override_hours

EffectiveOverrideHoursList: TypeAlias = list[
    "aws_sdk_connect.types.effective_override_hours.EffectiveOverrideHours"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveOverrideHoursList) -> list:
    import aws_sdk_connect.types.effective_override_hours

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.effective_override_hours.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectiveOverrideHoursList:
    import aws_sdk_connect.types.effective_override_hours

    out: EffectiveOverrideHoursList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.effective_override_hours.deserialize_json(item)
        )
    return out
