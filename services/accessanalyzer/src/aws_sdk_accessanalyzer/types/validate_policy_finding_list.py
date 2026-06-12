"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ValidatePolicyFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.validate_policy_finding

ValidatePolicyFindingList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.validate_policy_finding.ValidatePolicyFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePolicyFindingList) -> list:
    import aws_sdk_accessanalyzer.types.validate_policy_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.validate_policy_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ValidatePolicyFindingList:
    import aws_sdk_accessanalyzer.types.validate_policy_finding

    out: ValidatePolicyFindingList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.validate_policy_finding.deserialize_json(item)
        )
    return out
