"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaInputSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_criteria_input_step

RoutingCriteriaInputSteps: TypeAlias = list[
    "aws_sdk_connect.types.routing_criteria_input_step.RoutingCriteriaInputStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaInputSteps) -> list:
    import aws_sdk_connect.types.routing_criteria_input_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_criteria_input_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingCriteriaInputSteps:
    import aws_sdk_connect.types.routing_criteria_input_step

    out: RoutingCriteriaInputSteps = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_criteria_input_step.deserialize_json(item)
        )
    return out
