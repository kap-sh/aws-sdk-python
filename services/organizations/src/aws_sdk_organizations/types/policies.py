"""Generated from Smithy shape ``com.amazonaws.organizations#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy_summary

Policies: TypeAlias = list["aws_sdk_organizations.types.policy_summary.PolicySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Policies) -> list:
    import aws_sdk_organizations.types.policy_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.policy_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Policies:
    import aws_sdk_organizations.types.policy_summary

    out: Policies = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.policy_summary.deserialize_aws_json_1_1(item)
        )
    return out
