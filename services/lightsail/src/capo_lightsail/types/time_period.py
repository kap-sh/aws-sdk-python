"""Generated from Smithy shape ``com.amazonaws.lightsail#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date


class TimePeriod(TypedDict, closed=True):
    start: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The beginning of the time period. The start date is inclusive. For example, if <code>start</code> is <code>2017-01-01</code>, Lightsail for Research retrieves cost and usage data starting at <code>2017-01-01</code> up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.</p>"""
    end: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The end of the time period. The end date is exclusive. For example, if <code>end</code> is <code>2017-05-01</code>, Lightsail for Research retrieves cost and usage data from the start date up to, but not including, <code>2017-05-01</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimePeriod) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_lightsail.types.iso_date

        out["start"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["start"]
        )
    if "end" in value:
        import capo_lightsail.types.iso_date

        out["end"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(value["end"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import capo_lightsail.types.iso_date

        out["start"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["start"]
        )
    if "end" in data:
        import capo_lightsail.types.iso_date

        out["end"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(data["end"])
    return out
