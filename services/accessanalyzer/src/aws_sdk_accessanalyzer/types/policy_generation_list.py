"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PolicyGenerationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.policy_generation

PolicyGenerationList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.policy_generation.PolicyGeneration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationList) -> list:
    import aws_sdk_accessanalyzer.types.policy_generation

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.policy_generation.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyGenerationList:
    import aws_sdk_accessanalyzer.types.policy_generation

    out: PolicyGenerationList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.policy_generation.deserialize_json(item)
        )
    return out
