"""Generated from Smithy shape ``com.amazonaws.lightsail#EstimateByTime``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.currency
    import aws_sdk_lightsail.types.double
    import aws_sdk_lightsail.types.pricing_unit
    import aws_sdk_lightsail.types.time_period


class EstimateByTime(TypedDict):
    usage_cost: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The amount of cost or usage that's measured for the cost estimate.</p>"""
    pricing_unit: NotRequired["aws_sdk_lightsail.types.pricing_unit.PricingUnit"]
    """<p>The unit of measurement that's used for the cost estimate.</p>"""
    unit: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The number of pricing units used to calculate the total number of hours. For example, 1 unit equals 1 hour.</p>"""
    currency: NotRequired["aws_sdk_lightsail.types.currency.Currency"]
    """<p>The currency of the estimate in USD.</p>"""
    time_period: NotRequired["aws_sdk_lightsail.types.time_period.TimePeriod"]
    """<p>The period of time, in days, that an estimate covers. The period has a start date and an end date. The start date must come before the end date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EstimateByTime) -> dict:
    out: dict = {}
    if "usage_cost" in value:
        out["usageCost"] = value["usage_cost"]
    if "pricing_unit" in value:
        import aws_sdk_lightsail.types.pricing_unit

        out["pricingUnit"] = (
            aws_sdk_lightsail.types.pricing_unit.serialize_aws_json_1_1(
                value["pricing_unit"]
            )
        )
    if "unit" in value:
        out["unit"] = value["unit"]
    if "currency" in value:
        import aws_sdk_lightsail.types.currency

        out["currency"] = aws_sdk_lightsail.types.currency.serialize_aws_json_1_1(
            value["currency"]
        )
    if "time_period" in value:
        import aws_sdk_lightsail.types.time_period

        out["timePeriod"] = aws_sdk_lightsail.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EstimateByTime:
    out: EstimateByTime = {}  # type: ignore[typeddict-item]
    if "usageCost" in data:
        out["usage_cost"] = data["usageCost"]
    if "pricingUnit" in data:
        import aws_sdk_lightsail.types.pricing_unit

        out["pricing_unit"] = (
            aws_sdk_lightsail.types.pricing_unit.deserialize_aws_json_1_1(
                data["pricingUnit"]
            )
        )
    if "unit" in data:
        out["unit"] = data["unit"]
    if "currency" in data:
        import aws_sdk_lightsail.types.currency

        out["currency"] = aws_sdk_lightsail.types.currency.deserialize_aws_json_1_1(
            data["currency"]
        )
    if "timePeriod" in data:
        import aws_sdk_lightsail.types.time_period

        out["time_period"] = (
            aws_sdk_lightsail.types.time_period.deserialize_aws_json_1_1(
                data["timePeriod"]
            )
        )
    return out
