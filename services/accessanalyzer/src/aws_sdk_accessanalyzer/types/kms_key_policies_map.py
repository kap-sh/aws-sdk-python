"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsKeyPoliciesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.kms_key_policy
    import aws_sdk_accessanalyzer.types.policy_name

KmsKeyPoliciesMap: TypeAlias = dict[
    "aws_sdk_accessanalyzer.types.policy_name.PolicyName",
    "aws_sdk_accessanalyzer.types.kms_key_policy.KmsKeyPolicy",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: KmsKeyPoliciesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> KmsKeyPoliciesMap:
    out: KmsKeyPoliciesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
