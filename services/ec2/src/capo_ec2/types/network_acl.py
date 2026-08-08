"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAcl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_acl_association_list
    import capo_ec2.types.network_acl_entry_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class NetworkAcl(TypedDict, closed=True):
    associations: NotRequired[
        "capo_ec2.types.network_acl_association_list.NetworkAclAssociationList"
    ]
    """<p>Any associations between the network ACL and your subnets</p>"""
    entries: NotRequired["capo_ec2.types.network_acl_entry_list.NetworkAclEntryList"]
    """<p>The entries (rules) in the network ACL.</p>"""
    is_default: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default network ACL for the VPC.</p>"""
    network_acl_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network ACL.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the network ACL.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC for the network ACL.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the network ACL.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAcl, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associations" in value:
        import capo_ec2.types.network_acl_association_list

        capo_ec2.types.network_acl_association_list.serialize_ec2_query(
            value["associations"], pairs, f"{key_prefix}AssociationSet"
        )
    if "entries" in value:
        import capo_ec2.types.network_acl_entry_list

        capo_ec2.types.network_acl_entry_list.serialize_ec2_query(
            value["entries"], pairs, f"{key_prefix}EntrySet"
        )
    if "is_default" in value:
        pairs.append(
            (f"{key_prefix}Default", "true" if value["is_default"] else "false")
        )
    if "network_acl_id" in value:
        pairs.append((f"{key_prefix}NetworkAclId", str(value["network_acl_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))


def deserialize_ec2_query(el: Element) -> NetworkAcl:
    out: NetworkAcl = {}  # type: ignore[typeddict-item]
    if el.find("associationSet") is not None:
        import capo_ec2.types.network_acl_association_list

        out["associations"] = (
            capo_ec2.types.network_acl_association_list.deserialize_ec2_query(
                el, "associationSet"
            )
        )
    if el.find("entrySet") is not None:
        import capo_ec2.types.network_acl_entry_list

        out["entries"] = capo_ec2.types.network_acl_entry_list.deserialize_ec2_query(
            el, "entrySet"
        )
    child_is_default = el.find("default")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_network_acl_id = el.find("networkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    return out
