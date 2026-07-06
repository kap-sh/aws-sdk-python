"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.db_proxy_endpoint_status
    import aws_sdk_rds.types.db_proxy_endpoint_target_role
    import aws_sdk_rds.types.endpoint_network_type
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.string_list
    import aws_sdk_rds.types.t_stamp


class DBProxyEndpoint(TypedDict, closed=True):
    db_proxy_endpoint_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name for the DB proxy endpoint. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p>"""
    db_proxy_endpoint_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB proxy endpoint.</p>"""
    db_proxy_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier for the DB proxy that is associated with this DB proxy endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_rds.types.db_proxy_endpoint_status.DBProxyEndpointStatus"
    ]
    """<p>The current status of this DB proxy endpoint. A status of <code>available</code> means the endpoint is ready to handle requests. Other values indicate that you must wait for the endpoint to be ready, or take some action to resolve an issue.</p>"""
    vpc_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Provides the VPC ID of the DB proxy endpoint.</p>"""
    vpc_security_group_ids: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>Provides a list of VPC security groups that the DB proxy endpoint belongs to.</p>"""
    vpc_subnet_ids: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>The EC2 subnet IDs for the DB proxy endpoint.</p>"""
    endpoint: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</p>"""
    created_date: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the DB proxy endpoint was first created.</p>"""
    target_role: NotRequired[
        "aws_sdk_rds.types.db_proxy_endpoint_target_role.DBProxyEndpointTargetRole"
    ]
    """<p>A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.</p>"""
    is_default: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.</p>"""
    endpoint_network_type: NotRequired[
        "aws_sdk_rds.types.endpoint_network_type.EndpointNetworkType"
    ]
    """<p>The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy endpoint supports IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy endpoint supports IPv6 only.</p> </li> <li> <p> <code>DUAL</code> - The proxy endpoint supports both IPv4 and IPv6.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBProxyEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_endpoint_name" in value:
        pairs.append(
            (f"{prefix}.DBProxyEndpointName", str(value["db_proxy_endpoint_name"]))
        )
    if "db_proxy_endpoint_arn" in value:
        pairs.append(
            (f"{prefix}.DBProxyEndpointArn", str(value["db_proxy_endpoint_arn"]))
        )
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "status" in value:
        import aws_sdk_rds.types.db_proxy_endpoint_status

        aws_sdk_rds.types.db_proxy_endpoint_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "vpc_security_group_ids" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{prefix}.VpcSecurityGroupIds"
        )
    if "vpc_subnet_ids" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["vpc_subnet_ids"], pairs, f"{prefix}.VpcSubnetIds"
        )
    if "endpoint" in value:
        pairs.append((f"{prefix}.Endpoint", str(value["endpoint"])))
    if "created_date" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["created_date"], pairs, f"{prefix}.CreatedDate"
        )
    if "target_role" in value:
        import aws_sdk_rds.types.db_proxy_endpoint_target_role

        aws_sdk_rds.types.db_proxy_endpoint_target_role.serialize_query(
            value["target_role"], pairs, f"{prefix}.TargetRole"
        )
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "endpoint_network_type" in value:
        import aws_sdk_rds.types.endpoint_network_type

        aws_sdk_rds.types.endpoint_network_type.serialize_query(
            value["endpoint_network_type"], pairs, f"{prefix}.EndpointNetworkType"
        )


def deserialize_query(el: Element) -> DBProxyEndpoint:
    out: DBProxyEndpoint = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoint_name = el.find("DBProxyEndpointName")
    if child_db_proxy_endpoint_name is not None:
        out["db_proxy_endpoint_name"] = str(child_db_proxy_endpoint_name.text or "")
    child_db_proxy_endpoint_arn = el.find("DBProxyEndpointArn")
    if child_db_proxy_endpoint_arn is not None:
        out["db_proxy_endpoint_arn"] = str(child_db_proxy_endpoint_arn.text or "")
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_rds.types.db_proxy_endpoint_status

        out["status"] = aws_sdk_rds.types.db_proxy_endpoint_status.deserialize_query(
            child_status
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import aws_sdk_rds.types.string_list

        out["vpc_security_group_ids"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_vpc_security_group_ids
        )
    child_vpc_subnet_ids = el.find("VpcSubnetIds")
    if child_vpc_subnet_ids is not None:
        import aws_sdk_rds.types.string_list

        out["vpc_subnet_ids"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_vpc_subnet_ids
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import aws_sdk_rds.types.t_stamp

        out["created_date"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_created_date
        )
    child_target_role = el.find("TargetRole")
    if child_target_role is not None:
        import aws_sdk_rds.types.db_proxy_endpoint_target_role

        out["target_role"] = (
            aws_sdk_rds.types.db_proxy_endpoint_target_role.deserialize_query(
                child_target_role
            )
        )
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_endpoint_network_type = el.find("EndpointNetworkType")
    if child_endpoint_network_type is not None:
        import aws_sdk_rds.types.endpoint_network_type

        out["endpoint_network_type"] = (
            aws_sdk_rds.types.endpoint_network_type.deserialize_query(
                child_endpoint_network_type
            )
        )
    return out
