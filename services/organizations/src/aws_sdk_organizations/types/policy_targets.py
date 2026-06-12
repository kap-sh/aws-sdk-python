"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy_target_summary

PolicyTargets: TypeAlias = list[
    "aws_sdk_organizations.types.policy_target_summary.PolicyTargetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTargets) -> list:
    import aws_sdk_organizations.types.policy_target_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.policy_target_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyTargets:
    import aws_sdk_organizations.types.policy_target_summary

    out: PolicyTargets = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.policy_target_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
