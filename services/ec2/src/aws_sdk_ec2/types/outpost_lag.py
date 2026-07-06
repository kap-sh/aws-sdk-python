"""Generated from Smithy shape ``com.amazonaws.ec2#OutpostLag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.service_link_virtual_interface_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class OutpostLag(TypedDict, closed=True):
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Number (ARN) of the Outpost LAG.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Outpost LAG owner.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the Outpost LAG.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>The ID of the Outpost LAG.</p>"""
    local_gateway_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.LocalGatewayVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the local gateway virtual interfaces associated with the Outpost LAG.</p>"""
    service_link_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id_set.ServiceLinkVirtualInterfaceIdSet"
    ]
    """<p>The service link virtual interface IDs associated with the Outpost LAG.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the Outpost LAG.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OutpostLag, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "outpost_lag_id" in value:
        pairs.append((f"{prefix}.OutpostLagId", str(value["outpost_lag_id"])))
    if "local_gateway_virtual_interface_ids" in value:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set

        aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.serialize_ec2_query(
            value["local_gateway_virtual_interface_ids"],
            pairs,
            f"{prefix}.LocalGatewayVirtualInterfaceIdSet",
        )
    if "service_link_virtual_interface_ids" in value:
        import aws_sdk_ec2.types.service_link_virtual_interface_id_set

        aws_sdk_ec2.types.service_link_virtual_interface_id_set.serialize_ec2_query(
            value["service_link_virtual_interface_ids"],
            pairs,
            f"{prefix}.ServiceLinkVirtualInterfaceIdSet",
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> OutpostLag:
    out: OutpostLag = {}  # type: ignore[typeddict-item]
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_outpost_lag_id = el.find("OutpostLagId")
    if child_outpost_lag_id is not None:
        out["outpost_lag_id"] = str(child_outpost_lag_id.text or "")
    if el.find("LocalGatewayVirtualInterfaceIdSet") is not None:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set

        out["local_gateway_virtual_interface_ids"] = (
            aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.deserialize_ec2_query(
                el, "LocalGatewayVirtualInterfaceIdSet"
            )
        )
    if el.find("ServiceLinkVirtualInterfaceIdSet") is not None:
        import aws_sdk_ec2.types.service_link_virtual_interface_id_set

        out["service_link_virtual_interface_ids"] = (
            aws_sdk_ec2.types.service_link_virtual_interface_id_set.deserialize_ec2_query(
                el, "ServiceLinkVirtualInterfaceIdSet"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
