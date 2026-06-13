"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceDependentsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.next_token
    import aws_sdk_application_signals.types.service_dependents


class ListServiceDependentsOutput(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    service_dependents: (
        "aws_sdk_application_signals.types.service_dependents.ServiceDependents"
    )
    """<p>An array, where each object in the array contains information about one of the dependents of this service.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get next set of service dependents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceDependentsOutput) -> dict:
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
    import aws_sdk_application_signals.types.service_dependents

    out["ServiceDependents"] = (
        aws_sdk_application_signals.types.service_dependents.serialize_json(
            value["service_dependents"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceDependentsOutput:
    out: ListServiceDependentsOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceDependentsOutput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceDependentsOutput.end_time required")
    if "ServiceDependents" in data:
        import aws_sdk_application_signals.types.service_dependents

        out["service_dependents"] = (
            aws_sdk_application_signals.types.service_dependents.deserialize_json(
                data["ServiceDependents"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceDependentsOutput.service_dependents required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
