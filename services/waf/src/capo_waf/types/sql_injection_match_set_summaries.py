"""Generated from Smithy shape ``com.amazonaws.waf#SqlInjectionMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.sql_injection_match_set_summary

SqlInjectionMatchSetSummaries: TypeAlias = list[
    "capo_waf.types.sql_injection_match_set_summary.SqlInjectionMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetSummaries) -> list:
    import capo_waf.types.sql_injection_match_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_waf.types.sql_injection_match_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlInjectionMatchSetSummaries:
    import capo_waf.types.sql_injection_match_set_summary

    out: SqlInjectionMatchSetSummaries = []
    for item in data:
        out.append(
            capo_waf.types.sql_injection_match_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
