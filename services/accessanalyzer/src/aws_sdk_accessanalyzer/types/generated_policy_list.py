"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GeneratedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.generated_policy

GeneratedPolicyList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.generated_policy.GeneratedPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedPolicyList) -> list:
    import aws_sdk_accessanalyzer.types.generated_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.generated_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeneratedPolicyList:
    import aws_sdk_accessanalyzer.types.generated_policy

    out: GeneratedPolicyList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.generated_policy.deserialize_json(item))
    return out
