"""Generated from Smithy shape ``com.amazonaws.connect#AssociateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.flow_association_resource_type
    import aws_sdk_connect.types.instance_id


class AssociateFlowRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the resource.</p> <ul> <li> <p>Amazon Web Services End User Messaging SMS phone number ARN when using <code>SMS_PHONE_NUMBER</code> </p> </li> <li> <p>Amazon Web Services End User Messaging Social phone number ARN when using <code>WHATSAPP_MESSAGING_PHONE_NUMBER</code> </p> </li> </ul>"""
    flow_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    resource_type: "aws_sdk_connect.types.flow_association_resource_type.FlowAssociationResourceType"
    """<p>A valid resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateFlowRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["FlowId"] = value["flow_id"]
    import aws_sdk_connect.types.flow_association_resource_type

    out["ResourceType"] = (
        aws_sdk_connect.types.flow_association_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateFlowRequest:
    out: AssociateFlowRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("AssociateFlowRequest.resource_id required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("AssociateFlowRequest.flow_id required")
    if "ResourceType" in data:
        import aws_sdk_connect.types.flow_association_resource_type

        out["resource_type"] = (
            aws_sdk_connect.types.flow_association_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("AssociateFlowRequest.resource_type required")
    return out
