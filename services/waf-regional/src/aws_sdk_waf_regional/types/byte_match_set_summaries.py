"""Generated from Smithy shape ``com.amazonaws.wafregional#ByteMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.byte_match_set_summary

ByteMatchSetSummaries: TypeAlias = list[
    "aws_sdk_waf_regional.types.byte_match_set_summary.ByteMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSetSummaries) -> list:
    import aws_sdk_waf_regional.types.byte_match_set_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.byte_match_set_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ByteMatchSetSummaries:
    import aws_sdk_waf_regional.types.byte_match_set_summary

    out: ByteMatchSetSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.byte_match_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
