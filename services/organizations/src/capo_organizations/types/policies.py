"""Generated from Smithy shape ``com.amazonaws.organizations#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.policy_summary

Policies: TypeAlias = list["capo_organizations.types.policy_summary.PolicySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Policies) -> list:
    import capo_organizations.types.policy_summary

    out: list = []
    for item in value:
        out.append(capo_organizations.types.policy_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Policies:
    import capo_organizations.types.policy_summary

    out: Policies = []
    for item in data:
        out.append(
            capo_organizations.types.policy_summary.deserialize_aws_json_1_1(item)
        )
    return out
