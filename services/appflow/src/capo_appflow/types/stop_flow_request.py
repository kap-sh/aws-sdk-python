"""Generated from Smithy shape ``com.amazonaws.appflow#StopFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.flow_name


class StopFlowRequest(TypedDict, closed=True):
    flow_name: "capo_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    return out


def deserialize_json(data: dict) -> StopFlowRequest:
    out: StopFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("StopFlowRequest.flow_name required")
    return out
