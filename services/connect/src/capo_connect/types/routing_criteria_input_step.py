"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaInputStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.expression
    import capo_connect.types.routing_criteria_input_step_expiry


class RoutingCriteriaInputStep(TypedDict, closed=True):
    expiry: NotRequired[
        "capo_connect.types.routing_criteria_input_step_expiry.RoutingCriteriaInputStepExpiry"
    ]
    """<p>An object to specify the expiration of a routing step.</p>"""
    expression: NotRequired["capo_connect.types.expression.Expression"]
    """<p>A tagged union to specify expression for a routing step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaInputStep) -> dict:
    out: dict = {}
    if "expiry" in value:
        import capo_connect.types.routing_criteria_input_step_expiry

        out["Expiry"] = (
            capo_connect.types.routing_criteria_input_step_expiry.serialize_json(
                value["expiry"]
            )
        )
    if "expression" in value:
        import capo_connect.types.expression

        out["Expression"] = capo_connect.types.expression.serialize_json(
            value["expression"]
        )
    return out


def deserialize_json(data: dict) -> RoutingCriteriaInputStep:
    out: RoutingCriteriaInputStep = {}  # type: ignore[typeddict-item]
    if "Expiry" in data:
        import capo_connect.types.routing_criteria_input_step_expiry

        out["expiry"] = (
            capo_connect.types.routing_criteria_input_step_expiry.deserialize_json(
                data["Expiry"]
            )
        )
    if "Expression" in data:
        import capo_connect.types.expression

        out["expression"] = capo_connect.types.expression.deserialize_json(
            data["Expression"]
        )
    return out
