"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GeneratedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.generated_policy

GeneratedPolicyList: TypeAlias = list[
    "capo_accessanalyzer.types.generated_policy.GeneratedPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedPolicyList) -> list:
    import capo_accessanalyzer.types.generated_policy

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.generated_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeneratedPolicyList:
    import capo_accessanalyzer.types.generated_policy

    out: GeneratedPolicyList = []
    for item in data:
        out.append(capo_accessanalyzer.types.generated_policy.deserialize_json(item))
    return out
