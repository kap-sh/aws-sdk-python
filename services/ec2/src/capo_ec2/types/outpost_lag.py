"""Generated from Smithy shape ``com.amazonaws.ec2#OutpostLag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_virtual_interface_id_set
    import capo_ec2.types.outpost_lag_id
    import capo_ec2.types.service_link_virtual_interface_id_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class OutpostLag(TypedDict, closed=True):
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Number (ARN) of the Outpost LAG.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Outpost LAG owner.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the Outpost LAG.</p>"""
    outpost_lag_id: NotRequired["capo_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>The ID of the Outpost LAG.</p>"""
    local_gateway_virtual_interface_ids: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_id_set.LocalGatewayVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the local gateway virtual interfaces associated with the Outpost LAG.</p>"""
    service_link_virtual_interface_ids: NotRequired[
        "capo_ec2.types.service_link_virtual_interface_id_set.ServiceLinkVirtualInterfaceIdSet"
    ]
    """<p>The service link virtual interface IDs associated with the Outpost LAG.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the Outpost LAG.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OutpostLag, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "outpost_lag_id" in value:
        pairs.append((f"{key_prefix}OutpostLagId", str(value["outpost_lag_id"])))
    if "local_gateway_virtual_interface_ids" in value:
        import capo_ec2.types.local_gateway_virtual_interface_id_set

        capo_ec2.types.local_gateway_virtual_interface_id_set.serialize_ec2_query(
            value["local_gateway_virtual_interface_ids"],
            pairs,
            f"{key_prefix}LocalGatewayVirtualInterfaceIdSet",
        )
    if "service_link_virtual_interface_ids" in value:
        import capo_ec2.types.service_link_virtual_interface_id_set

        capo_ec2.types.service_link_virtual_interface_id_set.serialize_ec2_query(
            value["service_link_virtual_interface_ids"],
            pairs,
            f"{key_prefix}ServiceLinkVirtualInterfaceIdSet",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> OutpostLag:
    out: OutpostLag = {}  # type: ignore[typeddict-item]
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_outpost_lag_id = el.find("outpostLagId")
    if child_outpost_lag_id is not None:
        out["outpost_lag_id"] = str(child_outpost_lag_id.text or "")
    if el.find("localGatewayVirtualInterfaceIdSet") is not None:
        import capo_ec2.types.local_gateway_virtual_interface_id_set

        out["local_gateway_virtual_interface_ids"] = (
            capo_ec2.types.local_gateway_virtual_interface_id_set.deserialize_ec2_query(
                el, "localGatewayVirtualInterfaceIdSet"
            )
        )
    if el.find("serviceLinkVirtualInterfaceIdSet") is not None:
        import capo_ec2.types.service_link_virtual_interface_id_set

        out["service_link_virtual_interface_ids"] = (
            capo_ec2.types.service_link_virtual_interface_id_set.deserialize_ec2_query(
                el, "serviceLinkVirtualInterfaceIdSet"
            )
        )
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
