"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileAgentAvailabilityTimerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_availability_timer
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.routing_profile_id


class UpdateRoutingProfileAgentAvailabilityTimerRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    agent_availability_timer: (
        "aws_sdk_connect.types.agent_availability_timer.AgentAvailabilityTimer"
    )
    """<p>Whether agents with this routing profile will have their routing order calculated based on <i>time since their last inbound contact</i> or <i>longest idle time</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileAgentAvailabilityTimerRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.agent_availability_timer

    out["AgentAvailabilityTimer"] = (
        aws_sdk_connect.types.agent_availability_timer.serialize_json(
            value["agent_availability_timer"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileAgentAvailabilityTimerRequest:
    out: UpdateRoutingProfileAgentAvailabilityTimerRequest = {}  # type: ignore[typeddict-item]
    if "AgentAvailabilityTimer" in data:
        import aws_sdk_connect.types.agent_availability_timer

        out["agent_availability_timer"] = (
            aws_sdk_connect.types.agent_availability_timer.deserialize_json(
                data["AgentAvailabilityTimer"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingProfileAgentAvailabilityTimerRequest.agent_availability_timer required"
        )
    return out
