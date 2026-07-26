"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_inline_policy

ParameterPolicyList: TypeAlias = list[
    "capo_ssm.types.parameter_inline_policy.ParameterInlinePolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterPolicyList) -> list:
    import capo_ssm.types.parameter_inline_policy

    out: list = []
    for item in value:
        out.append(capo_ssm.types.parameter_inline_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterPolicyList:
    import capo_ssm.types.parameter_inline_policy

    out: ParameterPolicyList = []
    for item in data:
        out.append(
            capo_ssm.types.parameter_inline_policy.deserialize_aws_json_1_1(item)
        )
    return out
