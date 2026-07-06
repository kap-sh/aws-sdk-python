"""Generated from Smithy shape ``com.amazonaws.ssm#GetCalendarStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.calendar_name_or_arn_list
    import aws_sdk_ssm.types.iso8601_string


class GetCalendarStateRequest(TypedDict, closed=True):
    calendar_names: "aws_sdk_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList"
    """<p>The names of Amazon Resource Names (ARNs) of the Systems Manager documents (SSM documents) that represent the calendar entries for which you want to get the state.</p>"""
    at_time: NotRequired["aws_sdk_ssm.types.iso8601_string.ISO8601String"]
    r"""<p>(Optional) The specific time for which you want to get calendar state information, in <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> format. If you don't specify a value or <code>AtTime</code>, the current time is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalendarStateRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.calendar_name_or_arn_list

    out["CalendarNames"] = (
        aws_sdk_ssm.types.calendar_name_or_arn_list.serialize_aws_json_1_1(
            value["calendar_names"]
        )
    )
    if "at_time" in value:
        out["AtTime"] = value["at_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalendarStateRequest:
    out: GetCalendarStateRequest = {}  # type: ignore[typeddict-item]
    if "CalendarNames" in data:
        import aws_sdk_ssm.types.calendar_name_or_arn_list

        out["calendar_names"] = (
            aws_sdk_ssm.types.calendar_name_or_arn_list.deserialize_aws_json_1_1(
                data["CalendarNames"]
            )
        )
    else:
        raise DeserializationError("GetCalendarStateRequest.calendar_names required")
    if "AtTime" in data:
        out["at_time"] = data["AtTime"]
    return out
