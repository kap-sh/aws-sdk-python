"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.ec2_security_group_list
    import capo_redshift.types.ip_range_list
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class ClusterSecurityGroup(TypedDict, closed=True):
    cluster_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster security group to which the operation was applied.</p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>A description of the security group.</p>"""
    ec2_security_groups: NotRequired[
        "capo_redshift.types.ec2_security_group_list.EC2SecurityGroupList"
    ]
    """<p>A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.</p>"""
    ip_ranges: NotRequired["capo_redshift.types.ip_range_list.IPRangeList"]
    """<p>A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the cluster security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSecurityGroupName",
                str(value["cluster_security_group_name"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "ec2_security_groups" in value:
        import capo_redshift.types.ec2_security_group_list

        capo_redshift.types.ec2_security_group_list.serialize_query(
            value["ec2_security_groups"], pairs, f"{prefix}.EC2SecurityGroups"
        )
    if "ip_ranges" in value:
        import capo_redshift.types.ip_range_list

        capo_redshift.types.ip_range_list.serialize_query(
            value["ip_ranges"], pairs, f"{prefix}.IPRanges"
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> ClusterSecurityGroup:
    out: ClusterSecurityGroup = {}  # type: ignore[typeddict-item]
    child_cluster_security_group_name = el.find("ClusterSecurityGroupName")
    if child_cluster_security_group_name is not None:
        out["cluster_security_group_name"] = str(
            child_cluster_security_group_name.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_ec2_security_groups = el.find("EC2SecurityGroups")
    if child_ec2_security_groups is not None:
        import capo_redshift.types.ec2_security_group_list

        out["ec2_security_groups"] = (
            capo_redshift.types.ec2_security_group_list.deserialize_query(
                child_ec2_security_groups
            )
        )
    child_ip_ranges = el.find("IPRanges")
    if child_ip_ranges is not None:
        import capo_redshift.types.ip_range_list

        out["ip_ranges"] = capo_redshift.types.ip_range_list.deserialize_query(
            child_ip_ranges
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
