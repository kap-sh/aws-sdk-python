"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ExpressionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.string_list


class ExpressionFilter(TypedDict):
    key: NotRequired["str"]
    """<p> The key or attribute to filter on. </p>"""
    match_options: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.string_list.StringList"
    ]
    """<p> The match options for the filter (e.g., equals, contains). </p>"""
    values: NotRequired["aws_sdk_bcm_pricing_calculator.types.string_list.StringList"]
    """<p> The values to match against. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpressionFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "match_options" in value:
        import aws_sdk_bcm_pricing_calculator.types.string_list

        out["matchOptions"] = (
            aws_sdk_bcm_pricing_calculator.types.string_list.serialize_aws_json_1_0(
                value["match_options"]
            )
        )
    if "values" in value:
        import aws_sdk_bcm_pricing_calculator.types.string_list

        out["values"] = (
            aws_sdk_bcm_pricing_calculator.types.string_list.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpressionFilter:
    out: ExpressionFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "matchOptions" in data:
        import aws_sdk_bcm_pricing_calculator.types.string_list

        out["match_options"] = (
            aws_sdk_bcm_pricing_calculator.types.string_list.deserialize_aws_json_1_0(
                data["matchOptions"]
            )
        )
    if "values" in data:
        import aws_sdk_bcm_pricing_calculator.types.string_list

        out["values"] = (
            aws_sdk_bcm_pricing_calculator.types.string_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
