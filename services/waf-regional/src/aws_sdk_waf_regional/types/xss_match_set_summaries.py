"""Generated from Smithy shape ``com.amazonaws.wafregional#XssMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.xss_match_set_summary

XssMatchSetSummaries: TypeAlias = list[
    "aws_sdk_waf_regional.types.xss_match_set_summary.XssMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSetSummaries) -> list:
    import aws_sdk_waf_regional.types.xss_match_set_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.xss_match_set_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> XssMatchSetSummaries:
    import aws_sdk_waf_regional.types.xss_match_set_summary

    out: XssMatchSetSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.xss_match_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
