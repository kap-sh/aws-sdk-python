"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayVirtualInterfaceGroup(TypedDict, closed=True):
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    local_gateway_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.LocalGatewayVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the virtual interfaces.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface group.</p>"""
    local_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).</p>"""
    local_bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN for the local BGP configuration.</p>"""
    local_gateway_virtual_interface_group_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the local gateway virtual interface group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the virtual interface group.</p>"""
    configuration_state: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state.LocalGatewayVirtualInterfaceGroupConfigurationState"
    ]
    """<p>The current state of the local gateway virtual interface group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayVirtualInterfaceGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "local_gateway_virtual_interface_ids" in value:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set

        aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.serialize_ec2_query(
            value["local_gateway_virtual_interface_ids"],
            pairs,
            f"{prefix}.LocalGatewayVirtualInterfaceIdSet",
        )
    if "local_gateway_id" in value:
        pairs.append((f"{prefix}.LocalGatewayId", str(value["local_gateway_id"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "local_bgp_asn" in value:
        pairs.append((f"{prefix}.LocalBgpAsn", str(value["local_bgp_asn"])))
    if "local_bgp_asn_extended" in value:
        pairs.append(
            (f"{prefix}.LocalBgpAsnExtended", str(value["local_bgp_asn_extended"]))
        )
    if "local_gateway_virtual_interface_group_arn" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayVirtualInterfaceGroupArn",
                str(value["local_gateway_virtual_interface_group_arn"]),
            )
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "configuration_state" in value:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state

        aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state.serialize_ec2_query(
            value["configuration_state"], pairs, f"{prefix}.ConfigurationState"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayVirtualInterfaceGroup:
    out: LocalGatewayVirtualInterfaceGroup = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface_group_id = el.find(
        "LocalGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    if el.find("LocalGatewayVirtualInterfaceIdSet") is not None:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set

        out["local_gateway_virtual_interface_ids"] = (
            aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.deserialize_ec2_query(
                el, "LocalGatewayVirtualInterfaceIdSet"
            )
        )
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_local_bgp_asn = el.find("LocalBgpAsn")
    if child_local_bgp_asn is not None:
        out["local_bgp_asn"] = int(child_local_bgp_asn.text or "")
    child_local_bgp_asn_extended = el.find("LocalBgpAsnExtended")
    if child_local_bgp_asn_extended is not None:
        out["local_bgp_asn_extended"] = int(child_local_bgp_asn_extended.text or "")
    child_local_gateway_virtual_interface_group_arn = el.find(
        "LocalGatewayVirtualInterfaceGroupArn"
    )
    if child_local_gateway_virtual_interface_group_arn is not None:
        out["local_gateway_virtual_interface_group_arn"] = str(
            child_local_gateway_virtual_interface_group_arn.text or ""
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state

        out["configuration_state"] = (
            aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state.deserialize_ec2_query(
                child_configuration_state
            )
        )
    return out
