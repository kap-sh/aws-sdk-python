"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.geo_match_constraint

GeoMatchConstraints: TypeAlias = list[
    "aws_sdk_waf.types.geo_match_constraint.GeoMatchConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchConstraints) -> list:
    import aws_sdk_waf.types.geo_match_constraint

    out: list = []
    for item in value:
        out.append(aws_sdk_waf.types.geo_match_constraint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GeoMatchConstraints:
    import aws_sdk_waf.types.geo_match_constraint

    out: GeoMatchConstraints = []
    for item in data:
        out.append(
            aws_sdk_waf.types.geo_match_constraint.deserialize_aws_json_1_1(item)
        )
    return out
