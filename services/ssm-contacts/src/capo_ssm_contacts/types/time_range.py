"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time


class TimeRange(TypedDict, closed=True):
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The start of the time range.</p>"""
    end_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The end of the time range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm_contacts.types.date_time

        out["EndTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_ssm_contacts.types.date_time

        out["end_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
