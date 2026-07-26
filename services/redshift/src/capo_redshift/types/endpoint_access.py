"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.vpc_endpoint
    import capo_redshift.types.vpc_security_group_membership_list


class EndpointAccess(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier of the cluster associated with the endpoint.</p>"""
    resource_owner: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the cluster.</p>"""
    subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The subnet group name where Amazon Redshift chooses to deploy the endpoint.</p>"""
    endpoint_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the endpoint.</p>"""
    endpoint_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the endpoint.</p>"""
    endpoint_create_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) that the endpoint was created.</p>"""
    port: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The port number on which the cluster accepts incoming connections.</p>"""
    address: NotRequired["capo_redshift.types.string.String"]
    """<p>The DNS address of the endpoint.</p>"""
    vpc_security_groups: NotRequired[
        "capo_redshift.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>The security groups associated with the endpoint.</p>"""
    vpc_endpoint: NotRequired["capo_redshift.types.vpc_endpoint.VpcEndpoint"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAccess, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))
    if "subnet_group_name" in value:
        pairs.append((f"{prefix}.SubnetGroupName", str(value["subnet_group_name"])))
    if "endpoint_status" in value:
        pairs.append((f"{prefix}.EndpointStatus", str(value["endpoint_status"])))
    if "endpoint_name" in value:
        pairs.append((f"{prefix}.EndpointName", str(value["endpoint_name"])))
    if "endpoint_create_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["endpoint_create_time"], pairs, f"{prefix}.EndpointCreateTime"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "vpc_security_groups" in value:
        import capo_redshift.types.vpc_security_group_membership_list

        capo_redshift.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{prefix}.VpcSecurityGroups"
        )
    if "vpc_endpoint" in value:
        import capo_redshift.types.vpc_endpoint

        capo_redshift.types.vpc_endpoint.serialize_query(
            value["vpc_endpoint"], pairs, f"{prefix}.VpcEndpoint"
        )


def deserialize_query(el: Element) -> EndpointAccess:
    out: EndpointAccess = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_subnet_group_name = el.find("SubnetGroupName")
    if child_subnet_group_name is not None:
        out["subnet_group_name"] = str(child_subnet_group_name.text or "")
    child_endpoint_status = el.find("EndpointStatus")
    if child_endpoint_status is not None:
        out["endpoint_status"] = str(child_endpoint_status.text or "")
    child_endpoint_name = el.find("EndpointName")
    if child_endpoint_name is not None:
        out["endpoint_name"] = str(child_endpoint_name.text or "")
    child_endpoint_create_time = el.find("EndpointCreateTime")
    if child_endpoint_create_time is not None:
        import capo_redshift.types.t_stamp

        out["endpoint_create_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_endpoint_create_time
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import capo_redshift.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_redshift.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_groups
            )
        )
    child_vpc_endpoint = el.find("VpcEndpoint")
    if child_vpc_endpoint is not None:
        import capo_redshift.types.vpc_endpoint

        out["vpc_endpoint"] = capo_redshift.types.vpc_endpoint.deserialize_query(
            child_vpc_endpoint
        )
    return out
