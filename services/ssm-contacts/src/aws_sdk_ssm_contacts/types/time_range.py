"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time


class TimeRange(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The start of the time range.</p>"""
    end_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The end of the time range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
