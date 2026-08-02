"""Generated from Smithy shape ``com.amazonaws.ec2#TrunkInterfaceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.interface_protocol_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.trunk_interface_association_id


class TrunkInterfaceAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_ec2.types.trunk_interface_association_id.TrunkInterfaceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    branch_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the branch network interface.</p>"""
    trunk_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the trunk network interface.</p>"""
    interface_protocol: NotRequired[
        "capo_ec2.types.interface_protocol_type.InterfaceProtocolType"
    ]
    """<p>The interface protocol. Valid values are <code>VLAN</code> and <code>GRE</code>.</p>"""
    vlan_id: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN when you use the VLAN protocol.</p>"""
    gre_key: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The application key when you use the GRE protocol.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the trunk interface association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrunkInterfaceAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "branch_interface_id" in value:
        pairs.append(
            (f"{key_prefix}BranchInterfaceId", str(value["branch_interface_id"]))
        )
    if "trunk_interface_id" in value:
        pairs.append(
            (f"{key_prefix}TrunkInterfaceId", str(value["trunk_interface_id"]))
        )
    if "interface_protocol" in value:
        import capo_ec2.types.interface_protocol_type

        capo_ec2.types.interface_protocol_type.serialize_ec2_query(
            value["interface_protocol"], pairs, f"{key_prefix}InterfaceProtocol"
        )
    if "vlan_id" in value:
        pairs.append((f"{key_prefix}VlanId", str(value["vlan_id"])))
    if "gre_key" in value:
        pairs.append((f"{key_prefix}GreKey", str(value["gre_key"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TrunkInterfaceAssociation:
    out: TrunkInterfaceAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_branch_interface_id = el.find("BranchInterfaceId")
    if child_branch_interface_id is not None:
        out["branch_interface_id"] = str(child_branch_interface_id.text or "")
    child_trunk_interface_id = el.find("TrunkInterfaceId")
    if child_trunk_interface_id is not None:
        out["trunk_interface_id"] = str(child_trunk_interface_id.text or "")
    child_interface_protocol = el.find("InterfaceProtocol")
    if child_interface_protocol is not None:
        import capo_ec2.types.interface_protocol_type

        out["interface_protocol"] = (
            capo_ec2.types.interface_protocol_type.deserialize_ec2_query(
                child_interface_protocol
            )
        )
    child_vlan_id = el.find("VlanId")
    if child_vlan_id is not None:
        out["vlan_id"] = int(child_vlan_id.text or "")
    child_gre_key = el.find("GreKey")
    if child_gre_key is not None:
        out["gre_key"] = int(child_gre_key.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
