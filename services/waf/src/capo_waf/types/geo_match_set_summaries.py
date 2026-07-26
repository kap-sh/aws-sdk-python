"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.geo_match_set_summary

GeoMatchSetSummaries: TypeAlias = list[
    "capo_waf.types.geo_match_set_summary.GeoMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSetSummaries) -> list:
    import capo_waf.types.geo_match_set_summary

    out: list = []
    for item in value:
        out.append(capo_waf.types.geo_match_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GeoMatchSetSummaries:
    import capo_waf.types.geo_match_set_summary

    out: GeoMatchSetSummaries = []
    for item in data:
        out.append(capo_waf.types.geo_match_set_summary.deserialize_aws_json_1_1(item))
    return out
