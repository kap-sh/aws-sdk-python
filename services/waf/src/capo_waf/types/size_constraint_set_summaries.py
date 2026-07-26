"""Generated from Smithy shape ``com.amazonaws.waf#SizeConstraintSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.size_constraint_set_summary

SizeConstraintSetSummaries: TypeAlias = list[
    "capo_waf.types.size_constraint_set_summary.SizeConstraintSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetSummaries) -> list:
    import capo_waf.types.size_constraint_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_waf.types.size_constraint_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SizeConstraintSetSummaries:
    import capo_waf.types.size_constraint_set_summary

    out: SizeConstraintSetSummaries = []
    for item in data:
        out.append(
            capo_waf.types.size_constraint_set_summary.deserialize_aws_json_1_1(item)
        )
    return out
