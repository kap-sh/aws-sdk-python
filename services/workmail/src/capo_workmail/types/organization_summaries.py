"""Generated from Smithy shape ``com.amazonaws.workmail#OrganizationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.organization_summary

OrganizationSummaries: TypeAlias = list[
    "capo_workmail.types.organization_summary.OrganizationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationSummaries) -> list:
    import capo_workmail.types.organization_summary

    out: list = []
    for item in value:
        out.append(
            capo_workmail.types.organization_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationSummaries:
    import capo_workmail.types.organization_summary

    out: OrganizationSummaries = []
    for item in data:
        out.append(
            capo_workmail.types.organization_summary.deserialize_aws_json_1_1(item)
        )
    return out
