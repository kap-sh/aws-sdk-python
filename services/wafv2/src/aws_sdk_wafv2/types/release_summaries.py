"""Generated from Smithy shape ``com.amazonaws.wafv2#ReleaseSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.release_summary

ReleaseSummaries: TypeAlias = list["aws_sdk_wafv2.types.release_summary.ReleaseSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseSummaries) -> list:
    import aws_sdk_wafv2.types.release_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.release_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReleaseSummaries:
    import aws_sdk_wafv2.types.release_summary

    out: ReleaseSummaries = []
    for item in data:
        out.append(aws_sdk_wafv2.types.release_summary.deserialize_aws_json_1_1(item))
    return out
