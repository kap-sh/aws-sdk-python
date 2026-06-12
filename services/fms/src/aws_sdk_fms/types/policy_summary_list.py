"""Generated from Smithy shape ``com.amazonaws.fms#PolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy_summary

PolicySummaryList: TypeAlias = list["aws_sdk_fms.types.policy_summary.PolicySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicySummaryList) -> list:
    import aws_sdk_fms.types.policy_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.policy_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PolicySummaryList:
    import aws_sdk_fms.types.policy_summary

    out: PolicySummaryList = []
    for item in data:
        out.append(aws_sdk_fms.types.policy_summary.deserialize_aws_json_1_1(item))
    return out
