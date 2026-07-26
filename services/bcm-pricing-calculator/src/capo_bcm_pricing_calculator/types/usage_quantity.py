"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageQuantity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class UsageQuantity(TypedDict, closed=True):
    start_hour: NotRequired["datetime.datetime"]
    """<p> The start hour of the usage period. </p>"""
    unit: NotRequired["str"]
    """<p> The unit of measurement for the usage quantity. </p>"""
    amount: NotRequired["float"]
    """<p> The numeric value of the usage quantity. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageQuantity) -> dict:
    out: dict = {}
    if "start_hour" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["startHour"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_hour"]
            )
        )
    if "unit" in value:
        out["unit"] = value["unit"]
    if "amount" in value:
        out["amount"] = value["amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageQuantity:
    out: UsageQuantity = {}  # type: ignore[typeddict-item]
    if "startHour" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["start_hour"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startHour"]
            )
        )
    if "unit" in data:
        out["unit"] = data["unit"]
    if "amount" in data:
        out["amount"] = data["amount"]
    return out
