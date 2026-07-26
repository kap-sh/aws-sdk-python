"""Generated from Smithy shape ``com.amazonaws.ssm#PatchRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_rule

PatchRuleList: TypeAlias = list["capo_ssm.types.patch_rule.PatchRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchRuleList) -> list:
    import capo_ssm.types.patch_rule

    out: list = []
    for item in value:
        out.append(capo_ssm.types.patch_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchRuleList:
    import capo_ssm.types.patch_rule

    out: PatchRuleList = []
    for item in data:
        out.append(capo_ssm.types.patch_rule.deserialize_aws_json_1_1(item))
    return out
