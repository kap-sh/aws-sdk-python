"""Generated from Smithy shape ``com.amazonaws.mpa#PoliciesReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_reference

PoliciesReferences: TypeAlias = list[
    "aws_sdk_mpa.types.policy_reference.PolicyReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: PoliciesReferences) -> list:
    import aws_sdk_mpa.types.policy_reference

    out: list = []
    for item in value:
        out.append(aws_sdk_mpa.types.policy_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> PoliciesReferences:
    import aws_sdk_mpa.types.policy_reference

    out: PoliciesReferences = []
    for item in data:
        out.append(aws_sdk_mpa.types.policy_reference.deserialize_json(item))
    return out
