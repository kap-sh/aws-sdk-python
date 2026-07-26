"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.policy_type_summary

PolicyTypes: TypeAlias = list[
    "capo_organizations.types.policy_type_summary.PolicyTypeSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypes) -> list:
    import capo_organizations.types.policy_type_summary

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.policy_type_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyTypes:
    import capo_organizations.types.policy_type_summary

    out: PolicyTypes = []
    for item in data:
        out.append(
            capo_organizations.types.policy_type_summary.deserialize_aws_json_1_1(item)
        )
    return out
