"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateRoutingProfileQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.routing_profile_queue_reference_list


class DisassociateRoutingProfileQueuesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    queue_references: NotRequired[
        "aws_sdk_connect.types.routing_profile_queue_reference_list.RoutingProfileQueueReferenceList"
    ]
    """<p>The queues to disassociate from this routing profile.</p>"""
    manual_assignment_queue_references: NotRequired[
        "aws_sdk_connect.types.routing_profile_queue_reference_list.RoutingProfileQueueReferenceList"
    ]
    """<p>The manual assignment queues to disassociate with this routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateRoutingProfileQueuesRequest) -> dict:
    out: dict = {}
    if "queue_references" in value:
        import aws_sdk_connect.types.routing_profile_queue_reference_list

        out["QueueReferences"] = (
            aws_sdk_connect.types.routing_profile_queue_reference_list.serialize_json(
                value["queue_references"]
            )
        )
    if "manual_assignment_queue_references" in value:
        import aws_sdk_connect.types.routing_profile_queue_reference_list

        out["ManualAssignmentQueueReferences"] = (
            aws_sdk_connect.types.routing_profile_queue_reference_list.serialize_json(
                value["manual_assignment_queue_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateRoutingProfileQueuesRequest:
    out: DisassociateRoutingProfileQueuesRequest = {}  # type: ignore[typeddict-item]
    if "QueueReferences" in data:
        import aws_sdk_connect.types.routing_profile_queue_reference_list

        out["queue_references"] = (
            aws_sdk_connect.types.routing_profile_queue_reference_list.deserialize_json(
                data["QueueReferences"]
            )
        )
    if "ManualAssignmentQueueReferences" in data:
        import aws_sdk_connect.types.routing_profile_queue_reference_list

        out["manual_assignment_queue_references"] = (
            aws_sdk_connect.types.routing_profile_queue_reference_list.deserialize_json(
                data["ManualAssignmentQueueReferences"]
            )
        )
    return out
