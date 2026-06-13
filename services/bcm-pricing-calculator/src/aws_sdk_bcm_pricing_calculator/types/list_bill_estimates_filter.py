"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values
    import aws_sdk_bcm_pricing_calculator.types.match_option


class ListBillEstimatesFilter(TypedDict):
    name: "aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name.ListBillEstimatesFilterName"
    """<p> The name of the filter attribute. </p>"""
    values: "aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values.ListBillEstimatesFilterValues"
    """<p> The values to filter by. </p>"""
    match_option: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.match_option.MatchOption"
    ]
    """<p> The match option for the filter (e.g., equals, contains). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimatesFilter) -> dict:
    out: dict = {}
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name

    out["name"] = (
        aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name.serialize_aws_json_1_0(
            value["name"]
        )
    )
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values

    out["values"] = (
        aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    if "match_option" in value:
        import aws_sdk_bcm_pricing_calculator.types.match_option

        out["matchOption"] = (
            aws_sdk_bcm_pricing_calculator.types.match_option.serialize_aws_json_1_0(
                value["match_option"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillEstimatesFilter:
    out: ListBillEstimatesFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name

        out["name"] = (
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    else:
        raise DeserializationError("ListBillEstimatesFilter.name required")
    if "values" in data:
        import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values

        out["values"] = (
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("ListBillEstimatesFilter.values required")
    if "matchOption" in data:
        import aws_sdk_bcm_pricing_calculator.types.match_option

        out["match_option"] = (
            aws_sdk_bcm_pricing_calculator.types.match_option.deserialize_aws_json_1_0(
                data["matchOption"]
            )
        )
    return out
