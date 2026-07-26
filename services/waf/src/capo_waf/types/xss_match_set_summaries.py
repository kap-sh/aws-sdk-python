"""Generated from Smithy shape ``com.amazonaws.waf#XssMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.xss_match_set_summary

XssMatchSetSummaries: TypeAlias = list[
    "capo_waf.types.xss_match_set_summary.XssMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSetSummaries) -> list:
    import capo_waf.types.xss_match_set_summary

    out: list = []
    for item in value:
        out.append(capo_waf.types.xss_match_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> XssMatchSetSummaries:
    import capo_waf.types.xss_match_set_summary

    out: XssMatchSetSummaries = []
    for item in data:
        out.append(capo_waf.types.xss_match_set_summary.deserialize_aws_json_1_1(item))
    return out
