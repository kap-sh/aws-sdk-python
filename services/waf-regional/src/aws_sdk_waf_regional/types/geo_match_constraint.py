"""Generated from Smithy shape ``com.amazonaws.wafregional#GeoMatchConstraint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.geo_match_constraint_type
    import aws_sdk_waf_regional.types.geo_match_constraint_value


class GeoMatchConstraint(TypedDict):
    type: "aws_sdk_waf_regional.types.geo_match_constraint_type.GeoMatchConstraintType"
    """<p>The type of geographical area you want AWS WAF to search for. Currently <code>Country</code> is the only valid value.</p>"""
    value: (
        "aws_sdk_waf_regional.types.geo_match_constraint_value.GeoMatchConstraintValue"
    )
    """<p>The country that you want AWS WAF to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchConstraint) -> dict:
    out: dict = {}
    import aws_sdk_waf_regional.types.geo_match_constraint_type

    out["Type"] = (
        aws_sdk_waf_regional.types.geo_match_constraint_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import aws_sdk_waf_regional.types.geo_match_constraint_value

    out["Value"] = (
        aws_sdk_waf_regional.types.geo_match_constraint_value.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchConstraint:
    out: GeoMatchConstraint = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_waf_regional.types.geo_match_constraint_type

        out["type"] = (
            aws_sdk_waf_regional.types.geo_match_constraint_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("GeoMatchConstraint.type required")
    if "Value" in data:
        import aws_sdk_waf_regional.types.geo_match_constraint_value

        out["value"] = (
            aws_sdk_waf_regional.types.geo_match_constraint_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("GeoMatchConstraint.value required")
    return out
