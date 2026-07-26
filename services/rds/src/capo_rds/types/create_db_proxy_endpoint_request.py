"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBProxyEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_endpoint_name
    import capo_rds.types.db_proxy_endpoint_target_role
    import capo_rds.types.db_proxy_name
    import capo_rds.types.endpoint_network_type
    import capo_rds.types.string_list
    import capo_rds.types.tag_list


class CreateDBProxyEndpointRequest(TypedDict, closed=True):
    db_proxy_name: NotRequired["capo_rds.types.db_proxy_name.DBProxyName"]
    """<p>The name of the DB proxy associated with the DB proxy endpoint that you create.</p>"""
    db_proxy_endpoint_name: NotRequired[
        "capo_rds.types.db_proxy_endpoint_name.DBProxyEndpointName"
    ]
    """<p>The name of the DB proxy endpoint to create.</p>"""
    vpc_subnet_ids: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The VPC subnet IDs for the DB proxy endpoint that you create. You can specify a different set of subnet IDs than for the original DB proxy.</p>"""
    vpc_security_group_ids: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The VPC security group IDs for the DB proxy endpoint that you create. You can specify a different set of security group IDs than for the original DB proxy. The default is the default security group for the VPC.</p>"""
    target_role: NotRequired[
        "capo_rds.types.db_proxy_endpoint_target_role.DBProxyEndpointTargetRole"
    ]
    """<p>The role of the DB proxy endpoint. The role determines whether the endpoint can be used for read/write or only read operations. The default is <code>READ_WRITE</code>. The only role that proxies for RDS for Microsoft SQL Server support is <code>READ_WRITE</code>.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    endpoint_network_type: NotRequired[
        "capo_rds.types.endpoint_network_type.EndpointNetworkType"
    ]
    """<p>The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy endpoint supports IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy endpoint supports IPv6 only.</p> </li> <li> <p> <code>DUAL</code> - The proxy endpoint supports both IPv4 and IPv6.</p> </li> </ul> <p>Default: <code>IPV4</code> </p> <p>Constraints:</p> <ul> <li> <p>If you specify <code>IPV6</code> or <code>DUAL</code>, the VPC and all subnets must have an IPv6 CIDR block.</p> </li> <li> <p>If you specify <code>IPV6</code> or <code>DUAL</code>, the VPC tenancy cannot be <code>dedicated</code>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBProxyEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "db_proxy_endpoint_name" in value:
        pairs.append(
            (f"{prefix}.DBProxyEndpointName", str(value["db_proxy_endpoint_name"]))
        )
    if "vpc_subnet_ids" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["vpc_subnet_ids"], pairs, f"{prefix}.VpcSubnetIds"
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{prefix}.VpcSecurityGroupIds"
        )
    if "target_role" in value:
        import capo_rds.types.db_proxy_endpoint_target_role

        capo_rds.types.db_proxy_endpoint_target_role.serialize_query(
            value["target_role"], pairs, f"{prefix}.TargetRole"
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(value["tags"], pairs, f"{prefix}.Tags")
    if "endpoint_network_type" in value:
        import capo_rds.types.endpoint_network_type

        capo_rds.types.endpoint_network_type.serialize_query(
            value["endpoint_network_type"], pairs, f"{prefix}.EndpointNetworkType"
        )


def deserialize_query(el: Element) -> CreateDBProxyEndpointRequest:
    out: CreateDBProxyEndpointRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_db_proxy_endpoint_name = el.find("DBProxyEndpointName")
    if child_db_proxy_endpoint_name is not None:
        out["db_proxy_endpoint_name"] = str(child_db_proxy_endpoint_name.text or "")
    child_vpc_subnet_ids = el.find("VpcSubnetIds")
    if child_vpc_subnet_ids is not None:
        import capo_rds.types.string_list

        out["vpc_subnet_ids"] = capo_rds.types.string_list.deserialize_query(
            child_vpc_subnet_ids
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.string_list

        out["vpc_security_group_ids"] = capo_rds.types.string_list.deserialize_query(
            child_vpc_security_group_ids
        )
    child_target_role = el.find("TargetRole")
    if child_target_role is not None:
        import capo_rds.types.db_proxy_endpoint_target_role

        out["target_role"] = (
            capo_rds.types.db_proxy_endpoint_target_role.deserialize_query(
                child_target_role
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_endpoint_network_type = el.find("EndpointNetworkType")
    if child_endpoint_network_type is not None:
        import capo_rds.types.endpoint_network_type

        out["endpoint_network_type"] = (
            capo_rds.types.endpoint_network_type.deserialize_query(
                child_endpoint_network_type
            )
        )
    return out
