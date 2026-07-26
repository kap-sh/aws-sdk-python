"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.ip_set_summary

IPSetSummaries: TypeAlias = list["capo_waf_regional.types.ip_set_summary.IPSetSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetSummaries) -> list:
    import capo_waf_regional.types.ip_set_summary

    out: list = []
    for item in value:
        out.append(capo_waf_regional.types.ip_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IPSetSummaries:
    import capo_waf_regional.types.ip_set_summary

    out: IPSetSummaries = []
    for item in data:
        out.append(
            capo_waf_regional.types.ip_set_summary.deserialize_aws_json_1_1(item)
        )
    return out
