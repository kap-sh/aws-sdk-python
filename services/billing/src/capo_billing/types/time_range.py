"""Generated from Smithy shape ``com.amazonaws.billing#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class TimeRange(TypedDict, closed=True):
    begin_date_inclusive: NotRequired["datetime.datetime"]
    """<p> The inclusive start date of the time range. </p>"""
    end_date_inclusive: NotRequired["datetime.datetime"]
    """<p> The inclusive end date of the time range. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeRange) -> dict:
    out: dict = {}
    if "begin_date_inclusive" in value:
        import capo_billing.types._prelude.timestamp

        out["beginDateInclusive"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["begin_date_inclusive"]
            )
        )
    if "end_date_inclusive" in value:
        import capo_billing.types._prelude.timestamp

        out["endDateInclusive"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_date_inclusive"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "beginDateInclusive" in data:
        import capo_billing.types._prelude.timestamp

        out["begin_date_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["beginDateInclusive"]
            )
        )
    if "endDateInclusive" in data:
        import capo_billing.types._prelude.timestamp

        out["end_date_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDateInclusive"]
            )
        )
    return out
