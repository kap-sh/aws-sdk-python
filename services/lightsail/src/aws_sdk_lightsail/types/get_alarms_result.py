"""Generated from Smithy shape ``com.amazonaws.lightsail#GetAlarmsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.alarms_list
    import aws_sdk_lightsail.types.string


class GetAlarmsResult(TypedDict):
    alarms: NotRequired["aws_sdk_lightsail.types.alarms_list.AlarmsList"]
    """<p>An array of objects that describe the alarms.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetAlarms</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAlarmsResult) -> dict:
    out: dict = {}
    if "alarms" in value:
        import aws_sdk_lightsail.types.alarms_list

        out["alarms"] = aws_sdk_lightsail.types.alarms_list.serialize_aws_json_1_1(
            value["alarms"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAlarmsResult:
    out: GetAlarmsResult = {}  # type: ignore[typeddict-item]
    if "alarms" in data:
        import aws_sdk_lightsail.types.alarms_list

        out["alarms"] = aws_sdk_lightsail.types.alarms_list.deserialize_aws_json_1_1(
            data["alarms"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
