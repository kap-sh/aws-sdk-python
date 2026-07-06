"""Generated from Smithy shape ``com.amazonaws.redshift#CreateEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.vpc_security_group_id_list


class CreateEndpointAccessMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster identifier of the cluster to access.</p>"""
    resource_owner: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the cluster. This is only required if the cluster is in another Amazon Web Services account.</p>"""
    endpoint_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Redshift-managed VPC endpoint name.</p> <p>An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>"""
    subnet_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The subnet group from which Amazon Redshift chooses the subnet to deploy the endpoint.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))
    if "endpoint_name" in value:
        pairs.append((f"{prefix}.EndpointName", str(value["endpoint_name"])))
    if "subnet_group_name" in value:
        pairs.append((f"{prefix}.SubnetGroupName", str(value["subnet_group_name"])))
    if "vpc_security_group_ids" in value:
        import aws_sdk_redshift.types.vpc_security_group_id_list

        aws_sdk_redshift.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{prefix}.VpcSecurityGroupIds"
        )


def deserialize_query(el: Element) -> CreateEndpointAccessMessage:
    out: CreateEndpointAccessMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_endpoint_name = el.find("EndpointName")
    if child_endpoint_name is not None:
        out["endpoint_name"] = str(child_endpoint_name.text or "")
    child_subnet_group_name = el.find("SubnetGroupName")
    if child_subnet_group_name is not None:
        out["subnet_group_name"] = str(child_subnet_group_name.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import aws_sdk_redshift.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_redshift.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    return out
