"""Generated from Smithy shape ``com.amazonaws.connect#FlowAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.list_flow_association_resource_type


class FlowAssociationSummary(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The identifier of the resource.</p>"""
    flow_id: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The identifier of the flow.</p>"""
    resource_type: NotRequired[
        "aws_sdk_connect.types.list_flow_association_resource_type.ListFlowAssociationResourceType"
    ]
    """<p>The type of resource association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowAssociationSummary) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "flow_id" in value:
        out["FlowId"] = value["flow_id"]
    if "resource_type" in value:
        import aws_sdk_connect.types.list_flow_association_resource_type

        out["ResourceType"] = (
            aws_sdk_connect.types.list_flow_association_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowAssociationSummary:
    out: FlowAssociationSummary = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    if "ResourceType" in data:
        import aws_sdk_connect.types.list_flow_association_resource_type

        out["resource_type"] = (
            aws_sdk_connect.types.list_flow_association_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    return out
