"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.index
    import aws_sdk_connect.types.steps
    import aws_sdk_connect.types.timestamp


class RoutingCriteria(TypedDict):
    steps: NotRequired["aws_sdk_connect.types.steps.Steps"]
    """<p>List of routing steps. When Connect Customer does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.</p>"""
    activation_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the routing criteria is set to active. A routing criteria is activated when contact is transferred to a queue. ActivationTimestamp will be set on routing criteria for contacts in agent queue even though Routing criteria is never activated for contacts in agent queue.</p>"""
    index: NotRequired["aws_sdk_connect.types.index.Index"]
    """<p>Information about the index of the routing criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteria) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_connect.types.steps

        out["Steps"] = aws_sdk_connect.types.steps.serialize_json(value["steps"])
    if "activation_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["ActivationTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["activation_timestamp"]
        )
    if "index" in value:
        out["Index"] = value["index"]
    return out


def deserialize_json(data: dict) -> RoutingCriteria:
    out: RoutingCriteria = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import aws_sdk_connect.types.steps

        out["steps"] = aws_sdk_connect.types.steps.deserialize_json(data["Steps"])
    if "ActivationTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["activation_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["ActivationTimestamp"]
        )
    if "Index" in data:
        out["index"] = data["Index"]
    return out
