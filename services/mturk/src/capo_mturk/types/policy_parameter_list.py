"""Generated from Smithy shape ``com.amazonaws.mturk#PolicyParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.policy_parameter

PolicyParameterList: TypeAlias = list[
    "capo_mturk.types.policy_parameter.PolicyParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyParameterList) -> list:
    import capo_mturk.types.policy_parameter

    out: list = []
    for item in value:
        out.append(capo_mturk.types.policy_parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyParameterList:
    import capo_mturk.types.policy_parameter

    out: PolicyParameterList = []
    for item in data:
        out.append(capo_mturk.types.policy_parameter.deserialize_aws_json_1_1(item))
    return out
