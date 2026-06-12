"""Generated from Smithy shape ``com.amazonaws.iot#PolicyTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_target

PolicyTargets: TypeAlias = list["aws_sdk_iot.types.policy_target.PolicyTarget"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyTargets) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyTargets:
    return list(data)
