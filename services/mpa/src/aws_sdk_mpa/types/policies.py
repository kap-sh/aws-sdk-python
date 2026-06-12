"""Generated from Smithy shape ``com.amazonaws.mpa#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy

Policies: TypeAlias = list["aws_sdk_mpa.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: Policies) -> list:
    import aws_sdk_mpa.types.policy

    out: list = []
    for item in value:
        out.append(aws_sdk_mpa.types.policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Policies:
    import aws_sdk_mpa.types.policy

    out: Policies = []
    for item in data:
        out.append(aws_sdk_mpa.types.policy.deserialize_json(item))
    return out
