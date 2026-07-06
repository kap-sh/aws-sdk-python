"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceStatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.next_token
    import aws_sdk_application_signals.types.service_states


class ListServiceStatesOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    service_states: "aws_sdk_application_signals.types.service_states.ServiceStates"
    """<p>An array of structures, where each structure contains information about the state of one service, including its latest change events such as deployments.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of service states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceStatesOutput) -> dict:
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
    import aws_sdk_application_signals.types.service_states

    out["ServiceStates"] = (
        aws_sdk_application_signals.types.service_states.serialize_json(
            value["service_states"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceStatesOutput:
    out: ListServiceStatesOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesOutput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesOutput.end_time required")
    if "ServiceStates" in data:
        import aws_sdk_application_signals.types.service_states

        out["service_states"] = (
            aws_sdk_application_signals.types.service_states.deserialize_json(
                data["ServiceStates"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesOutput.service_states required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
