"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_criteria_input_steps


class RoutingCriteriaInput(TypedDict, closed=True):
    steps: NotRequired[
        "aws_sdk_connect.types.routing_criteria_input_steps.RoutingCriteriaInputSteps"
    ]
    """<p>When Connect Customer does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaInput) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_connect.types.routing_criteria_input_steps

        out["Steps"] = (
            aws_sdk_connect.types.routing_criteria_input_steps.serialize_json(
                value["steps"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingCriteriaInput:
    out: RoutingCriteriaInput = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import aws_sdk_connect.types.routing_criteria_input_steps

        out["steps"] = (
            aws_sdk_connect.types.routing_criteria_input_steps.deserialize_json(
                data["Steps"]
            )
        )
    return out
