"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class BillInterval(TypedDict, closed=True):
    start: NotRequired["datetime.datetime"]
    """<p> The start date and time of the interval. </p>"""
    end: NotRequired["datetime.datetime"]
    """<p> The end date and time of the interval. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillInterval) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["start"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start"]
            )
        )
    if "end" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["end"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillInterval:
    out: BillInterval = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["start"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["start"]
            )
        )
    if "end" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["end"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["end"]
            )
        )
    return out
