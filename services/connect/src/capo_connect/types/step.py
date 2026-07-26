"""Generated from Smithy shape ``com.amazonaws.connect#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.expiry
    import capo_connect.types.expression
    import capo_connect.types.routing_criteria_step_status


class Step(TypedDict, closed=True):
    expiry: NotRequired["capo_connect.types.expiry.Expiry"]
    """<p>An object to specify the expiration of a routing step.</p>"""
    expression: NotRequired["capo_connect.types.expression.Expression"]
    """<p>A tagged union to specify expression for a routing step.</p>"""
    status: NotRequired[
        "capo_connect.types.routing_criteria_step_status.RoutingCriteriaStepStatus"
    ]
    """<p>Represents status of the Routing step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    if "expiry" in value:
        import capo_connect.types.expiry

        out["Expiry"] = capo_connect.types.expiry.serialize_json(value["expiry"])
    if "expression" in value:
        import capo_connect.types.expression

        out["Expression"] = capo_connect.types.expression.serialize_json(
            value["expression"]
        )
    if "status" in value:
        import capo_connect.types.routing_criteria_step_status

        out["Status"] = capo_connect.types.routing_criteria_step_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if "Expiry" in data:
        import capo_connect.types.expiry

        out["expiry"] = capo_connect.types.expiry.deserialize_json(data["Expiry"])
    if "Expression" in data:
        import capo_connect.types.expression

        out["expression"] = capo_connect.types.expression.deserialize_json(
            data["Expression"]
        )
    if "Status" in data:
        import capo_connect.types.routing_criteria_step_status

        out["status"] = (
            capo_connect.types.routing_criteria_step_status.deserialize_json(
                data["Status"]
            )
        )
    return out
