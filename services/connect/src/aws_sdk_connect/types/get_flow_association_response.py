"""Generated from Smithy shape ``com.amazonaws.connect#GetFlowAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.flow_association_resource_type


class GetFlowAssociationResponse(TypedDict):
    resource_id: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The identifier of the resource.</p>"""
    flow_id: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The identifier of the flow.</p>"""
    resource_type: NotRequired[
        "aws_sdk_connect.types.flow_association_resource_type.FlowAssociationResourceType"
    ]
    """<p>A valid resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowAssociationResponse) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "flow_id" in value:
        out["FlowId"] = value["flow_id"]
    if "resource_type" in value:
        import aws_sdk_connect.types.flow_association_resource_type

        out["ResourceType"] = (
            aws_sdk_connect.types.flow_association_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFlowAssociationResponse:
    out: GetFlowAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    if "ResourceType" in data:
        import aws_sdk_connect.types.flow_association_resource_type

        out["resource_type"] = (
            aws_sdk_connect.types.flow_association_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    return out
