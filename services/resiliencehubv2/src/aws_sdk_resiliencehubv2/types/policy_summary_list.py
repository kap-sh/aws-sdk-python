"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.policy_summary

PolicySummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.policy_summary.PolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicySummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.policy_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.policy_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicySummaryList:
    import aws_sdk_resiliencehubv2.types.policy_summary

    out: PolicySummaryList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.policy_summary.deserialize_json(item))
    return out
