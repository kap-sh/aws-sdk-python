"""Generated from Smithy shape ``com.amazonaws.connect#Dimensions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_identifier
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.queue_reference
    import aws_sdk_connect.types.routing_expression
    import aws_sdk_connect.types.routing_profile_reference
    import aws_sdk_connect.types.subtype
    import aws_sdk_connect.types.validation_test_type


class Dimensions(TypedDict):
    queue: NotRequired["aws_sdk_connect.types.queue_reference.QueueReference"]
    """<p>Information about the queue for which metrics are returned.</p>"""
    channel: NotRequired["aws_sdk_connect.types.channel.Channel"]
    """<p>The channel used for grouping and filters.</p>"""
    routing_profile: NotRequired[
        "aws_sdk_connect.types.routing_profile_reference.RoutingProfileReference"
    ]
    routing_step_expression: NotRequired[
        "aws_sdk_connect.types.routing_expression.RoutingExpression"
    ]
    """<p>The expression of a step in a routing criteria.</p>"""
    agent_status: NotRequired[
        "aws_sdk_connect.types.agent_status_identifier.AgentStatusIdentifier"
    ]
    """<p>Information about the agent status assigned to the user.</p>"""
    subtype: NotRequired["aws_sdk_connect.types.subtype.Subtype"]
    """<p>The subtype of the channel used for the contact.</p>"""
    validation_test_type: NotRequired[
        "aws_sdk_connect.types.validation_test_type.ValidationTestType"
    ]
    """<p>The testing and simulation type</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimensions) -> dict:
    out: dict = {}
    if "queue" in value:
        import aws_sdk_connect.types.queue_reference

        out["Queue"] = aws_sdk_connect.types.queue_reference.serialize_json(
            value["queue"]
        )
    if "channel" in value:
        import aws_sdk_connect.types.channel

        out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    if "routing_profile" in value:
        import aws_sdk_connect.types.routing_profile_reference

        out["RoutingProfile"] = (
            aws_sdk_connect.types.routing_profile_reference.serialize_json(
                value["routing_profile"]
            )
        )
    if "routing_step_expression" in value:
        out["RoutingStepExpression"] = value["routing_step_expression"]
    if "agent_status" in value:
        import aws_sdk_connect.types.agent_status_identifier

        out["AgentStatus"] = (
            aws_sdk_connect.types.agent_status_identifier.serialize_json(
                value["agent_status"]
            )
        )
    if "subtype" in value:
        out["Subtype"] = value["subtype"]
    if "validation_test_type" in value:
        out["ValidationTestType"] = value["validation_test_type"]
    return out


def deserialize_json(data: dict) -> Dimensions:
    out: Dimensions = {}  # type: ignore[typeddict-item]
    if "Queue" in data:
        import aws_sdk_connect.types.queue_reference

        out["queue"] = aws_sdk_connect.types.queue_reference.deserialize_json(
            data["Queue"]
        )
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    if "RoutingProfile" in data:
        import aws_sdk_connect.types.routing_profile_reference

        out["routing_profile"] = (
            aws_sdk_connect.types.routing_profile_reference.deserialize_json(
                data["RoutingProfile"]
            )
        )
    if "RoutingStepExpression" in data:
        out["routing_step_expression"] = data["RoutingStepExpression"]
    if "AgentStatus" in data:
        import aws_sdk_connect.types.agent_status_identifier

        out["agent_status"] = (
            aws_sdk_connect.types.agent_status_identifier.deserialize_json(
                data["AgentStatus"]
            )
        )
    if "Subtype" in data:
        out["subtype"] = data["Subtype"]
    if "ValidationTestType" in data:
        out["validation_test_type"] = data["ValidationTestType"]
    return out
