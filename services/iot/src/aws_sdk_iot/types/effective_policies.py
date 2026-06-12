"""Generated from Smithy shape ``com.amazonaws.iot#EffectivePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.effective_policy

EffectivePolicies: TypeAlias = list[
    "aws_sdk_iot.types.effective_policy.EffectivePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePolicies) -> list:
    import aws_sdk_iot.types.effective_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.effective_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectivePolicies:
    import aws_sdk_iot.types.effective_policy

    out: EffectivePolicies = []
    for item in data:
        out.append(aws_sdk_iot.types.effective_policy.deserialize_json(item))
    return out
