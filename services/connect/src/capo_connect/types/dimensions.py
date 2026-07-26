"""Generated from Smithy shape ``com.amazonaws.connect#Dimensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_identifier
    import capo_connect.types.channel
    import capo_connect.types.queue_reference
    import capo_connect.types.routing_expression
    import capo_connect.types.routing_profile_reference
    import capo_connect.types.subtype
    import capo_connect.types.validation_test_type


class Dimensions(TypedDict, closed=True):
    queue: NotRequired["capo_connect.types.queue_reference.QueueReference"]
    """<p>Information about the queue for which metrics are returned.</p>"""
    channel: NotRequired["capo_connect.types.channel.Channel"]
    """<p>The channel used for grouping and filters.</p>"""
    routing_profile: NotRequired[
        "capo_connect.types.routing_profile_reference.RoutingProfileReference"
    ]
    routing_step_expression: NotRequired[
        "capo_connect.types.routing_expression.RoutingExpression"
    ]
    """<p>The expression of a step in a routing criteria.</p>"""
    agent_status: NotRequired[
        "capo_connect.types.agent_status_identifier.AgentStatusIdentifier"
    ]
    """<p>Information about the agent status assigned to the user.</p>"""
    subtype: NotRequired["capo_connect.types.subtype.Subtype"]
    """<p>The subtype of the channel used for the contact.</p>"""
    validation_test_type: NotRequired[
        "capo_connect.types.validation_test_type.ValidationTestType"
    ]
    """<p>The testing and simulation type</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimensions) -> dict:
    out: dict = {}
    if "queue" in value:
        import capo_connect.types.queue_reference

        out["Queue"] = capo_connect.types.queue_reference.serialize_json(value["queue"])
    if "channel" in value:
        import capo_connect.types.channel

        out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    if "routing_profile" in value:
        import capo_connect.types.routing_profile_reference

        out["RoutingProfile"] = (
            capo_connect.types.routing_profile_reference.serialize_json(
                value["routing_profile"]
            )
        )
    if "routing_step_expression" in value:
        out["RoutingStepExpression"] = value["routing_step_expression"]
    if "agent_status" in value:
        import capo_connect.types.agent_status_identifier

        out["AgentStatus"] = capo_connect.types.agent_status_identifier.serialize_json(
            value["agent_status"]
        )
    if "subtype" in value:
        out["Subtype"] = value["subtype"]
    if "validation_test_type" in value:
        out["ValidationTestType"] = value["validation_test_type"]
    return out


def deserialize_json(data: dict) -> Dimensions:
    out: Dimensions = {}  # type: ignore[typeddict-item]
    if "Queue" in data:
        import capo_connect.types.queue_reference

        out["queue"] = capo_connect.types.queue_reference.deserialize_json(
            data["Queue"]
        )
    if "Channel" in data:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    if "RoutingProfile" in data:
        import capo_connect.types.routing_profile_reference

        out["routing_profile"] = (
            capo_connect.types.routing_profile_reference.deserialize_json(
                data["RoutingProfile"]
            )
        )
    if "RoutingStepExpression" in data:
        out["routing_step_expression"] = data["RoutingStepExpression"]
    if "AgentStatus" in data:
        import capo_connect.types.agent_status_identifier

        out["agent_status"] = (
            capo_connect.types.agent_status_identifier.deserialize_json(
                data["AgentStatus"]
            )
        )
    if "Subtype" in data:
        out["subtype"] = data["Subtype"]
    if "ValidationTestType" in data:
        out["validation_test_type"] = data["ValidationTestType"]
    return out
