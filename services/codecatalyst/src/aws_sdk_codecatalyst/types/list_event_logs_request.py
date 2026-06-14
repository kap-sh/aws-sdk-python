"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListEventLogsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.timestamp


class ListEventLogsRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    start_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The date and time when you want to start retrieving events, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    end_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time after which you do not want any events retrieved, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    event_name: NotRequired["str"]
    """<p>The name of the event.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventLogsRequest) -> dict:
    out: dict = {}
    import aws_sdk_codecatalyst.types.timestamp

    out["startTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_codecatalyst.types.timestamp

    out["endTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["end_time"]
    )
    if "event_name" in value:
        out["eventName"] = value["event_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEventLogsRequest:
    out: ListEventLogsRequest = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["start_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("ListEventLogsRequest.start_time required")
    if "endTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["end_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("ListEventLogsRequest.end_time required")
    if "eventName" in data:
        out["event_name"] = data["eventName"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
