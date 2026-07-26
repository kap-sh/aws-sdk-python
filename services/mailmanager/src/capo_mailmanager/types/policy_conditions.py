"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.policy_condition

PolicyConditions: TypeAlias = list[
    "capo_mailmanager.types.policy_condition.PolicyCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyConditions) -> list:
    import capo_mailmanager.types.policy_condition

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.policy_condition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyConditions:
    import capo_mailmanager.types.policy_condition

    out: PolicyConditions = []
    for item in data:
        out.append(
            capo_mailmanager.types.policy_condition.deserialize_aws_json_1_0(item)
        )
    return out
