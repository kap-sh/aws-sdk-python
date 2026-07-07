"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListEventLogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.event_log_entries


class ListEventLogsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    items: "aws_sdk_codecatalyst.types.event_log_entries.EventLogEntries"
    """<p>Information about each event retrieved in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventLogsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_codecatalyst.types.event_log_entries

    out["items"] = aws_sdk_codecatalyst.types.event_log_entries.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> ListEventLogsResponse:
    out: ListEventLogsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_codecatalyst.types.event_log_entries

        out["items"] = aws_sdk_codecatalyst.types.event_log_entries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListEventLogsResponse.items required")
    return out
