"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ListMonitorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmonitor.types.monitor_list


class ListMonitorsOutput(TypedDict, closed=True):
    monitors: "capo_networkmonitor.types.monitor_list.MonitorList"
    """<p>Lists individual details about each of your monitors.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsOutput) -> dict:
    out: dict = {}
    import capo_networkmonitor.types.monitor_list

    out["monitors"] = capo_networkmonitor.types.monitor_list.serialize_json(
        value["monitors"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitorsOutput:
    out: ListMonitorsOutput = {}  # type: ignore[typeddict-item]
    if "monitors" in data:
        import capo_networkmonitor.types.monitor_list

        out["monitors"] = capo_networkmonitor.types.monitor_list.deserialize_json(
            data["monitors"]
        )
    else:
        raise DeserializationError("ListMonitorsOutput.monitors required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
