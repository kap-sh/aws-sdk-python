"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_association_state
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type
    import aws_sdk_ec2.types.transit_gateway_policy_table_id


class TransitGatewayPolicyTableAssociation(TypedDict):
    transit_gateway_policy_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId"
    ]
    """<p>The ID of the transit gateway policy table.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource ID of the transit gateway attachment.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The resource type for the transit gateway policy table association.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_association_state.TransitGatewayAssociationState"
    ]
    """<p>The state of the transit gateway policy table association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_policy_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayPolicyTableId",
                str(value["transit_gateway_policy_table_id"]),
            )
        )
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_association_state

        aws_sdk_ec2.types.transit_gateway_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableAssociation:
    out: TransitGatewayPolicyTableAssociation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table_id = el.find("TransitGatewayPolicyTableId")
    if child_transit_gateway_policy_table_id is not None:
        out["transit_gateway_policy_table_id"] = str(
            child_transit_gateway_policy_table_id.text or ""
        )
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_association_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
