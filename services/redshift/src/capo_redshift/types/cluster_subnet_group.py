"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.subnet_list
    import capo_redshift.types.tag_list
    import capo_redshift.types.value_string_list


class ClusterSubnetGroup(TypedDict, closed=True):
    cluster_subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster subnet group.</p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of the cluster subnet group.</p>"""
    vpc_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The VPC ID of the cluster subnet group.</p>"""
    subnet_group_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the cluster subnet group. Possible values are <code>Complete</code>, <code>Incomplete</code> and <code>Invalid</code>. </p>"""
    subnets: NotRequired["capo_redshift.types.subnet_list.SubnetList"]
    """<p>A list of the VPC <a>Subnet</a> elements. </p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the cluster subnet group.</p>"""
    supported_cluster_ip_address_types: NotRequired[
        "capo_redshift.types.value_string_list.ValueStringList"
    ]
    """<p>The IP address types supported by this cluster subnet group. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSubnetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_group_status" in value:
        pairs.append((f"{prefix}.SubnetGroupStatus", str(value["subnet_group_status"])))
    if "subnets" in value:
        import capo_redshift.types.subnet_list

        capo_redshift.types.subnet_list.serialize_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "supported_cluster_ip_address_types" in value:
        import capo_redshift.types.value_string_list

        capo_redshift.types.value_string_list.serialize_query(
            value["supported_cluster_ip_address_types"],
            pairs,
            f"{prefix}.SupportedClusterIpAddressTypes",
        )


def deserialize_query(el: Element) -> ClusterSubnetGroup:
    out: ClusterSubnetGroup = {}  # type: ignore[typeddict-item]
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_group_status = el.find("SubnetGroupStatus")
    if child_subnet_group_status is not None:
        out["subnet_group_status"] = str(child_subnet_group_status.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_redshift.types.subnet_list

        out["subnets"] = capo_redshift.types.subnet_list.deserialize_query(
            child_subnets
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    child_supported_cluster_ip_address_types = el.find("SupportedClusterIpAddressTypes")
    if child_supported_cluster_ip_address_types is not None:
        import capo_redshift.types.value_string_list

        out["supported_cluster_ip_address_types"] = (
            capo_redshift.types.value_string_list.deserialize_query(
                child_supported_cluster_ip_address_types
            )
        )
    return out
