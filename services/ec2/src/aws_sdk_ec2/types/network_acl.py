"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAcl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_acl_association_list
    import aws_sdk_ec2.types.network_acl_entry_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkAcl(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.network_acl_association_list.NetworkAclAssociationList"
    ]
    """<p>Any associations between the network ACL and your subnets</p>"""
    entries: NotRequired["aws_sdk_ec2.types.network_acl_entry_list.NetworkAclEntryList"]
    """<p>The entries (rules) in the network ACL.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default network ACL for the VPC.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network ACL.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the network ACL.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the network ACL.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the network ACL.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAcl, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "associations" in value:
        import aws_sdk_ec2.types.network_acl_association_list

        aws_sdk_ec2.types.network_acl_association_list.serialize_ec2_query(
            value["associations"], pairs, f"{prefix}.AssociationSet"
        )
    if "entries" in value:
        import aws_sdk_ec2.types.network_acl_entry_list

        aws_sdk_ec2.types.network_acl_entry_list.serialize_ec2_query(
            value["entries"], pairs, f"{prefix}.EntrySet"
        )
    if "is_default" in value:
        pairs.append((f"{prefix}.Default", "true" if value["is_default"] else "false"))
    if "network_acl_id" in value:
        pairs.append((f"{prefix}.NetworkAclId", str(value["network_acl_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))


def deserialize_ec2_query(el: Element) -> NetworkAcl:
    out: NetworkAcl = {}  # type: ignore[typeddict-item]
    if el.find("AssociationSet") is not None:
        import aws_sdk_ec2.types.network_acl_association_list

        out["associations"] = (
            aws_sdk_ec2.types.network_acl_association_list.deserialize_ec2_query(
                el, "AssociationSet"
            )
        )
    if el.find("EntrySet") is not None:
        import aws_sdk_ec2.types.network_acl_entry_list

        out["entries"] = aws_sdk_ec2.types.network_acl_entry_list.deserialize_ec2_query(
            el, "EntrySet"
        )
    child_is_default = el.find("Default")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_network_acl_id = el.find("NetworkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    return out
