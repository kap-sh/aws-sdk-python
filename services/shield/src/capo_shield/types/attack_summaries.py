"""Generated from Smithy shape ``com.amazonaws.shield#AttackSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.attack_summary

AttackSummaries: TypeAlias = list["capo_shield.types.attack_summary.AttackSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackSummaries) -> list:
    import capo_shield.types.attack_summary

    out: list = []
    for item in value:
        out.append(capo_shield.types.attack_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttackSummaries:
    import capo_shield.types.attack_summary

    out: AttackSummaries = []
    for item in data:
        out.append(capo_shield.types.attack_summary.deserialize_aws_json_1_1(item))
    return out
