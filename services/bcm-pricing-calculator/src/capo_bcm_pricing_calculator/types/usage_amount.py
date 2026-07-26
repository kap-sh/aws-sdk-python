"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class UsageAmount(TypedDict, closed=True):
    start_hour: "datetime.datetime"
    """<p> The start hour of the usage period. </p>"""
    amount: "float"
    """<p> The usage amount for the period. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageAmount) -> dict:
    out: dict = {}
    import capo_bcm_pricing_calculator.types._prelude.timestamp

    out["startHour"] = (
        capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_hour"]
        )
    )
    out["amount"] = value["amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageAmount:
    out: UsageAmount = {}  # type: ignore[typeddict-item]
    if "startHour" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["start_hour"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startHour"]
            )
        )
    else:
        raise DeserializationError("UsageAmount.start_hour required")
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        raise DeserializationError("UsageAmount.amount required")
    return out
