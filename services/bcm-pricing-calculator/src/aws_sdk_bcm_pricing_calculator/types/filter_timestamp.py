"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#FilterTimestamp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class FilterTimestamp(TypedDict, closed=True):
    after_timestamp: NotRequired["datetime.datetime"]
    """<p> Include results after this timestamp. </p>"""
    before_timestamp: NotRequired["datetime.datetime"]
    """<p> Include results before this timestamp. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterTimestamp) -> dict:
    out: dict = {}
    if "after_timestamp" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["afterTimestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["after_timestamp"]
            )
        )
    if "before_timestamp" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["beforeTimestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["before_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FilterTimestamp:
    out: FilterTimestamp = {}  # type: ignore[typeddict-item]
    if "afterTimestamp" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["after_timestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["afterTimestamp"]
            )
        )
    if "beforeTimestamp" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["before_timestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["beforeTimestamp"]
            )
        )
    return out
