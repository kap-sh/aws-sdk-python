"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListMonitorsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_list


class ListMonitorsOutput(TypedDict):
    monitors: "aws_sdk_networkflowmonitor.types.monitor_list.MonitorList"
    """<p>The monitors that are in an account.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.monitor_list

    out["monitors"] = aws_sdk_networkflowmonitor.types.monitor_list.serialize_json(
        value["monitors"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitorsOutput:
    out: ListMonitorsOutput = {}  # type: ignore[typeddict-item]
    if "monitors" in data:
        import aws_sdk_networkflowmonitor.types.monitor_list

        out["monitors"] = (
            aws_sdk_networkflowmonitor.types.monitor_list.deserialize_json(
                data["monitors"]
            )
        )
    else:
        raise DeserializationError("ListMonitorsOutput.monitors required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
