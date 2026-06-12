"""Generated from Smithy shape ``com.amazonaws.wafregional#SizeConstraintSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.size_constraint_set_summary

SizeConstraintSetSummaries: TypeAlias = list[
    "aws_sdk_waf_regional.types.size_constraint_set_summary.SizeConstraintSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetSummaries) -> list:
    import aws_sdk_waf_regional.types.size_constraint_set_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.size_constraint_set_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SizeConstraintSetSummaries:
    import aws_sdk_waf_regional.types.size_constraint_set_summary

    out: SizeConstraintSetSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.size_constraint_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
