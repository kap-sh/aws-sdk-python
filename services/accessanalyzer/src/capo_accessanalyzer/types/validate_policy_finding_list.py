"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ValidatePolicyFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.validate_policy_finding

ValidatePolicyFindingList: TypeAlias = list[
    "capo_accessanalyzer.types.validate_policy_finding.ValidatePolicyFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePolicyFindingList) -> list:
    import capo_accessanalyzer.types.validate_policy_finding

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.validate_policy_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ValidatePolicyFindingList:
    import capo_accessanalyzer.types.validate_policy_finding

    out: ValidatePolicyFindingList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.validate_policy_finding.deserialize_json(item)
        )
    return out
