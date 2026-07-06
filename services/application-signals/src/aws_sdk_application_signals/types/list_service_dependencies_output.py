"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceDependenciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.next_token
    import aws_sdk_application_signals.types.service_dependencies


class ListServiceDependenciesOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    service_dependencies: (
        "aws_sdk_application_signals.types.service_dependencies.ServiceDependencies"
    )
    """<p>An array, where each object in the array contains information about one of the dependencies of this service.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get next set of service dependencies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceDependenciesOutput) -> dict:
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
    import aws_sdk_application_signals.types.service_dependencies

    out["ServiceDependencies"] = (
        aws_sdk_application_signals.types.service_dependencies.serialize_json(
            value["service_dependencies"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceDependenciesOutput:
    out: ListServiceDependenciesOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceDependenciesOutput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceDependenciesOutput.end_time required")
    if "ServiceDependencies" in data:
        import aws_sdk_application_signals.types.service_dependencies

        out["service_dependencies"] = (
            aws_sdk_application_signals.types.service_dependencies.deserialize_json(
                data["ServiceDependencies"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceDependenciesOutput.service_dependencies required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
