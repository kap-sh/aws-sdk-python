"""Generated from Smithy shape ``com.amazonaws.wafregional#GeoMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.geo_match_set_update

GeoMatchSetUpdates: TypeAlias = list[
    "capo_waf_regional.types.geo_match_set_update.GeoMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSetUpdates) -> list:
    import capo_waf_regional.types.geo_match_set_update

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.geo_match_set_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GeoMatchSetUpdates:
    import capo_waf_regional.types.geo_match_set_update

    out: GeoMatchSetUpdates = []
    for item in data:
        out.append(
            capo_waf_regional.types.geo_match_set_update.deserialize_aws_json_1_1(item)
        )
    return out
