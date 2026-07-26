"""Generated from Smithy shape ``com.amazonaws.wafv2#APIKeySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.api_key_summary

APIKeySummaries: TypeAlias = list["capo_wafv2.types.api_key_summary.APIKeySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APIKeySummaries) -> list:
    import capo_wafv2.types.api_key_summary

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.api_key_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> APIKeySummaries:
    import capo_wafv2.types.api_key_summary

    out: APIKeySummaries = []
    for item in data:
        out.append(capo_wafv2.types.api_key_summary.deserialize_aws_json_1_1(item))
    return out
