"""Generated from Smithy shape ``com.amazonaws.wafregional#GeoMatchConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.geo_match_constraint

GeoMatchConstraints: TypeAlias = list[
    "capo_waf_regional.types.geo_match_constraint.GeoMatchConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchConstraints) -> list:
    import capo_waf_regional.types.geo_match_constraint

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.geo_match_constraint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GeoMatchConstraints:
    import capo_waf_regional.types.geo_match_constraint

    out: GeoMatchConstraints = []
    for item in data:
        out.append(
            capo_waf_regional.types.geo_match_constraint.deserialize_aws_json_1_1(item)
        )
    return out
