"""Generated from Smithy shape ``com.amazonaws.connect#CreateRoutingProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_availability_timer
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.media_concurrencies
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.routing_profile_description
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list
    import aws_sdk_connect.types.routing_profile_name
    import aws_sdk_connect.types.routing_profile_queue_config_list
    import aws_sdk_connect.types.tag_map


class CreateRoutingProfileRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.routing_profile_name.RoutingProfileName"
    """<p>The name of the routing profile. Must not be more than 127 characters.</p>"""
    description: (
        "aws_sdk_connect.types.routing_profile_description.RoutingProfileDescription"
    )
    """<p>Description of the routing profile. Must not be more than 250 characters.</p>"""
    default_outbound_queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The default outbound queue for the routing profile.</p>"""
    queue_configs: NotRequired[
        "aws_sdk_connect.types.routing_profile_queue_config_list.RoutingProfileQueueConfigList"
    ]
    r"""<p>The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.</p> <p>The limit of 10 array members applies to the maximum number of <code>RoutingProfileQueueConfig</code> objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Connect Customer service quotas</a>. </p>"""
    manual_assignment_queue_configs: NotRequired[
        "aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list.RoutingProfileManualAssignmentQueueConfigList"
    ]
    """<p>The manual assignment queues associated with the routing profile. If no queue is added, agents and supervisors can't pick or assign any contacts from this routing profile. The limit of 10 array members applies to the maximum number of RoutingProfileManualAssignmentQueueConfig objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in Connect Customer service quotas.</p> <p>Note: Use this config for chat, email, and task contacts. It does not support voice contacts.</p>"""
    media_concurrencies: "aws_sdk_connect.types.media_concurrencies.MediaConcurrencies"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP) for this routing profile.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    agent_availability_timer: NotRequired[
        "aws_sdk_connect.types.agent_availability_timer.AgentAvailabilityTimer"
    ]
    """<p>Whether agents with this routing profile will have their routing order calculated based on <i>longest idle time</i> or <i>time since their last inbound contact</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoutingProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["DefaultOutboundQueueId"] = value["default_outbound_queue_id"]
    if "queue_configs" in value:
        import aws_sdk_connect.types.routing_profile_queue_config_list

        out["QueueConfigs"] = (
            aws_sdk_connect.types.routing_profile_queue_config_list.serialize_json(
                value["queue_configs"]
            )
        )
    if "manual_assignment_queue_configs" in value:
        import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list

        out["ManualAssignmentQueueConfigs"] = (
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list.serialize_json(
                value["manual_assignment_queue_configs"]
            )
        )
    import aws_sdk_connect.types.media_concurrencies

    out["MediaConcurrencies"] = (
        aws_sdk_connect.types.media_concurrencies.serialize_json(
            value["media_concurrencies"]
        )
    )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "agent_availability_timer" in value:
        import aws_sdk_connect.types.agent_availability_timer

        out["AgentAvailabilityTimer"] = (
            aws_sdk_connect.types.agent_availability_timer.serialize_json(
                value["agent_availability_timer"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRoutingProfileRequest:
    out: CreateRoutingProfileRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRoutingProfileRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateRoutingProfileRequest.description required")
    if "DefaultOutboundQueueId" in data:
        out["default_outbound_queue_id"] = data["DefaultOutboundQueueId"]
    else:
        raise DeserializationError(
            "CreateRoutingProfileRequest.default_outbound_queue_id required"
        )
    if "QueueConfigs" in data:
        import aws_sdk_connect.types.routing_profile_queue_config_list

        out["queue_configs"] = (
            aws_sdk_connect.types.routing_profile_queue_config_list.deserialize_json(
                data["QueueConfigs"]
            )
        )
    if "ManualAssignmentQueueConfigs" in data:
        import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list

        out["manual_assignment_queue_configs"] = (
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_list.deserialize_json(
                data["ManualAssignmentQueueConfigs"]
            )
        )
    if "MediaConcurrencies" in data:
        import aws_sdk_connect.types.media_concurrencies

        out["media_concurrencies"] = (
            aws_sdk_connect.types.media_concurrencies.deserialize_json(
                data["MediaConcurrencies"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRoutingProfileRequest.media_concurrencies required"
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "AgentAvailabilityTimer" in data:
        import aws_sdk_connect.types.agent_availability_timer

        out["agent_availability_timer"] = (
            aws_sdk_connect.types.agent_availability_timer.deserialize_json(
                data["AgentAvailabilityTimer"]
            )
        )
    return out
