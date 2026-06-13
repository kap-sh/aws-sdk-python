"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListEntityEventsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.change_events
    import aws_sdk_application_signals.types.next_token


class ListEntityEventsOutput(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned change events apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned change events apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>"""
    change_events: "aws_sdk_application_signals.types.change_events.ChangeEvents"
    """<p>An array of structures, where each structure contains information about one change event that occurred for the specified entity during the requested time period.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of change events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntityEventsOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types._prelude.timestamp

    out["StartTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_application_signals.types._prelude.timestamp

    out["EndTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    )
    import aws_sdk_application_signals.types.change_events

    out["ChangeEvents"] = (
        aws_sdk_application_signals.types.change_events.serialize_json(
            value["change_events"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntityEventsOutput:
    out: ListEntityEventsOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListEntityEventsOutput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListEntityEventsOutput.end_time required")
    if "ChangeEvents" in data:
        import aws_sdk_application_signals.types.change_events

        out["change_events"] = (
            aws_sdk_application_signals.types.change_events.deserialize_json(
                data["ChangeEvents"]
            )
        )
    else:
        raise DeserializationError("ListEntityEventsOutput.change_events required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
