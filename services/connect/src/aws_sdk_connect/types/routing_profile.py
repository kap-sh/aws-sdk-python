"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_availability_timer
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.associated_queue_id_list
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.long
    import aws_sdk_connect.types.media_concurrencies
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.routing_profile_description
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.routing_profile_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class RoutingProfile(TypedDict):
    instance_id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: NotRequired["aws_sdk_connect.types.routing_profile_name.RoutingProfileName"]
    """<p>The name of the routing profile.</p>"""
    routing_profile_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the routing profile.</p>"""
    routing_profile_id: NotRequired[
        "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    ]
    """<p>The identifier of the routing profile.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.routing_profile_description.RoutingProfileDescription"
    ]
    """<p>The description of the routing profile.</p>"""
    media_concurrencies: NotRequired[
        "aws_sdk_connect.types.media_concurrencies.MediaConcurrencies"
    ]
    """<p>The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.</p>"""
    default_outbound_queue_id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The identifier of the default outbound queue for this routing profile.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    number_of_associated_queues: NotRequired["aws_sdk_connect.types.long.Long"]
    """<p>The number of associated queues in routing profile.</p>"""
    number_of_associated_manual_assignment_queues: NotRequired[
        "aws_sdk_connect.types.long.Long"
    ]
    """<p>The number of associated manual assignment queues in routing profile.</p>"""
    number_of_associated_users: NotRequired["aws_sdk_connect.types.long.Long"]
    """<p>The number of associated users in routing profile.</p>"""
    agent_availability_timer: NotRequired[
        "aws_sdk_connect.types.agent_availability_timer.AgentAvailabilityTimer"
    ]
    """<p>Whether agents with this routing profile will have their routing order calculated based on <i>time since their last inbound contact</i> or <i>longest idle time</i>. </p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    is_default: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether this a default routing profile.</p>"""
    associated_queue_ids: NotRequired[
        "aws_sdk_connect.types.associated_queue_id_list.AssociatedQueueIdList"
    ]
    """<p>The IDs of the associated queue.</p>"""
    associated_manual_assignment_queue_ids: NotRequired[
        "aws_sdk_connect.types.associated_queue_id_list.AssociatedQueueIdList"
    ]
    """<p>The IDs of the associated manual assignment queues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfile) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "routing_profile_arn" in value:
        out["RoutingProfileArn"] = value["routing_profile_arn"]
    if "routing_profile_id" in value:
        out["RoutingProfileId"] = value["routing_profile_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "media_concurrencies" in value:
        import aws_sdk_connect.types.media_concurrencies

        out["MediaConcurrencies"] = (
            aws_sdk_connect.types.media_concurrencies.serialize_json(
                value["media_concurrencies"]
            )
        )
    if "default_outbound_queue_id" in value:
        out["DefaultOutboundQueueId"] = value["default_outbound_queue_id"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "number_of_associated_queues" in value:
        out["NumberOfAssociatedQueues"] = value["number_of_associated_queues"]
    if "number_of_associated_manual_assignment_queues" in value:
        out["NumberOfAssociatedManualAssignmentQueues"] = value[
            "number_of_associated_manual_assignment_queues"
        ]
    if "number_of_associated_users" in value:
        out["NumberOfAssociatedUsers"] = value["number_of_associated_users"]
    if "agent_availability_timer" in value:
        import aws_sdk_connect.types.agent_availability_timer

        out["AgentAvailabilityTimer"] = (
            aws_sdk_connect.types.agent_availability_timer.serialize_json(
                value["agent_availability_timer"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    out["IsDefault"] = value.get("is_default", False)
    if "associated_queue_ids" in value:
        import aws_sdk_connect.types.associated_queue_id_list

        out["AssociatedQueueIds"] = (
            aws_sdk_connect.types.associated_queue_id_list.serialize_json(
                value["associated_queue_ids"]
            )
        )
    if "associated_manual_assignment_queue_ids" in value:
        import aws_sdk_connect.types.associated_queue_id_list

        out["AssociatedManualAssignmentQueueIds"] = (
            aws_sdk_connect.types.associated_queue_id_list.serialize_json(
                value["associated_manual_assignment_queue_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingProfile:
    out: RoutingProfile = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RoutingProfileArn" in data:
        out["routing_profile_arn"] = data["RoutingProfileArn"]
    if "RoutingProfileId" in data:
        out["routing_profile_id"] = data["RoutingProfileId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "MediaConcurrencies" in data:
        import aws_sdk_connect.types.media_concurrencies

        out["media_concurrencies"] = (
            aws_sdk_connect.types.media_concurrencies.deserialize_json(
                data["MediaConcurrencies"]
            )
        )
    if "DefaultOutboundQueueId" in data:
        out["default_outbound_queue_id"] = data["DefaultOutboundQueueId"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "NumberOfAssociatedQueues" in data:
        out["number_of_associated_queues"] = data["NumberOfAssociatedQueues"]
    if "NumberOfAssociatedManualAssignmentQueues" in data:
        out["number_of_associated_manual_assignment_queues"] = data[
            "NumberOfAssociatedManualAssignmentQueues"
        ]
    if "NumberOfAssociatedUsers" in data:
        out["number_of_associated_users"] = data["NumberOfAssociatedUsers"]
    if "AgentAvailabilityTimer" in data:
        import aws_sdk_connect.types.agent_availability_timer

        out["agent_availability_timer"] = (
            aws_sdk_connect.types.agent_availability_timer.deserialize_json(
                data["AgentAvailabilityTimer"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if "AssociatedQueueIds" in data:
        import aws_sdk_connect.types.associated_queue_id_list

        out["associated_queue_ids"] = (
            aws_sdk_connect.types.associated_queue_id_list.deserialize_json(
                data["AssociatedQueueIds"]
            )
        )
    if "AssociatedManualAssignmentQueueIds" in data:
        import aws_sdk_connect.types.associated_queue_id_list

        out["associated_manual_assignment_queue_ids"] = (
            aws_sdk_connect.types.associated_queue_id_list.deserialize_json(
                data["AssociatedManualAssignmentQueueIds"]
            )
        )
    return out
