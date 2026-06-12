"""Generated from Smithy shape ``com.amazonaws.sesv2#PolicyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.policy
    import aws_sdk_sesv2.types.policy_name

PolicyMap: TypeAlias = dict[
    "aws_sdk_sesv2.types.policy_name.PolicyName", "aws_sdk_sesv2.types.policy.Policy"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PolicyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PolicyMap:
    out: PolicyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
