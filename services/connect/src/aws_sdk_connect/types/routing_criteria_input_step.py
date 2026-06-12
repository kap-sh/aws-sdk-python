"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaInputStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.expression
    import aws_sdk_connect.types.routing_criteria_input_step_expiry


class RoutingCriteriaInputStep(TypedDict):
    expiry: NotRequired[
        "aws_sdk_connect.types.routing_criteria_input_step_expiry.RoutingCriteriaInputStepExpiry"
    ]
    """<p>An object to specify the expiration of a routing step.</p>"""
    expression: NotRequired["aws_sdk_connect.types.expression.Expression"]
    """<p>A tagged union to specify expression for a routing step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaInputStep) -> dict:
    out: dict = {}
    if "expiry" in value:
        import aws_sdk_connect.types.routing_criteria_input_step_expiry

        out["Expiry"] = (
            aws_sdk_connect.types.routing_criteria_input_step_expiry.serialize_json(
                value["expiry"]
            )
        )
    if "expression" in value:
        import aws_sdk_connect.types.expression

        out["Expression"] = aws_sdk_connect.types.expression.serialize_json(
            value["expression"]
        )
    return out


def deserialize_json(data: dict) -> RoutingCriteriaInputStep:
    out: RoutingCriteriaInputStep = {}  # type: ignore[typeddict-item]
    if "Expiry" in data:
        import aws_sdk_connect.types.routing_criteria_input_step_expiry

        out["expiry"] = (
            aws_sdk_connect.types.routing_criteria_input_step_expiry.deserialize_json(
                data["Expiry"]
            )
        )
    if "Expression" in data:
        import aws_sdk_connect.types.expression

        out["expression"] = aws_sdk_connect.types.expression.deserialize_json(
            data["Expression"]
        )
    return out
