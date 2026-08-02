"""Generated from Smithy shape ``com.amazonaws.rds#DBProxy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.db_proxy_status
    import capo_rds.types.endpoint_network_type
    import capo_rds.types.integer
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.t_stamp
    import capo_rds.types.target_connection_network_type
    import capo_rds.types.user_auth_config_info_list


class DBProxy(TypedDict, closed=True):
    db_proxy_name: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the proxy. This name must be unique for all proxies owned by your Amazon Web Services account in the specified Amazon Web Services Region.</p>"""
    db_proxy_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the proxy.</p>"""
    status: NotRequired["capo_rds.types.db_proxy_status.DBProxyStatus"]
    """<p>The current status of this proxy. A status of <code>available</code> means the proxy is ready to handle requests. Other values indicate that you must wait for the proxy to be ready, or take some action to resolve an issue.</p>"""
    engine_family: NotRequired["capo_rds.types.string.String"]
    """<p>The kinds of databases that the proxy can connect to. This value determines which database network protocol the proxy recognizes when it interprets network traffic to and from the database. <code>MYSQL</code> supports Aurora MySQL, RDS for MariaDB, and RDS for MySQL databases. <code>POSTGRESQL</code> supports Aurora PostgreSQL and RDS for PostgreSQL databases. <code>SQLSERVER</code> supports RDS for Microsoft SQL Server databases.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the VPC ID of the DB proxy.</p>"""
    vpc_security_group_ids: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>Provides a list of VPC security groups that the proxy belongs to.</p>"""
    vpc_subnet_ids: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The EC2 subnet IDs for the proxy.</p>"""
    default_auth_scheme: NotRequired["capo_rds.types.string.String"]
    """<p>The default authentication scheme that the proxy uses for client connections to the proxy and connections from the proxy to the underlying database. Valid values are <code>NONE</code> and <code>IAM_AUTH</code>. When set to <code>IAM_AUTH</code>, the proxy uses end-to-end IAM authentication to connect to the database. </p>"""
    auth: NotRequired[
        "capo_rds.types.user_auth_config_info_list.UserAuthConfigInfoList"
    ]
    """<p>One or more data structures specifying the authorization mechanism to connect to the associated RDS DB instance or Aurora DB cluster.</p>"""
    role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that the proxy uses to access Amazon Secrets Manager.</p>"""
    endpoint: NotRequired["capo_rds.types.string.String"]
    """<p>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</p>"""
    require_tls: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether Transport Layer Security (TLS) encryption is required for connections to the proxy.</p>"""
    idle_client_timeout: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The number of seconds a connection to the proxy can have no activity before the proxy drops the client connection. The proxy keeps the underlying database connection open and puts it back into the connection pool for reuse by later connection requests.</p> <p>Default: 1800 (30 minutes)</p> <p>Constraints: 1 to 28,800</p>"""
    debug_logging: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the proxy logs detailed connection and query information. When you enable <code>DebugLogging</code>, the proxy captures connection details and connection pool behavior from your queries. Debug logging increases CloudWatch costs and can impact proxy performance. Enable this option only when you need to troubleshoot connection or performance issues.</p>"""
    created_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the proxy was first created.</p>"""
    updated_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the proxy was last updated.</p>"""
    endpoint_network_type: NotRequired[
        "capo_rds.types.endpoint_network_type.EndpointNetworkType"
    ]
    """<p>The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy endpoint supports IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy endpoint supports IPv6 only.</p> </li> <li> <p> <code>DUAL</code> - The proxy endpoint supports both IPv4 and IPv6.</p> </li> </ul>"""
    target_connection_network_type: NotRequired[
        "capo_rds.types.target_connection_network_type.TargetConnectionNetworkType"
    ]
    """<p>The network type that the proxy uses to connect to the target database. The network type determines the IP version that the proxy uses for connections to the database.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy connects to the database using IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy connects to the database using IPv6 only.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(value: DBProxy, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_name" in value:
        pairs.append((f"{key_prefix}DBProxyName", str(value["db_proxy_name"])))
    if "db_proxy_arn" in value:
        pairs.append((f"{key_prefix}DBProxyArn", str(value["db_proxy_arn"])))
    if "status" in value:
        import capo_rds.types.db_proxy_status

        capo_rds.types.db_proxy_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "engine_family" in value:
        pairs.append((f"{key_prefix}EngineFamily", str(value["engine_family"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpc_security_group_ids" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "vpc_subnet_ids" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["vpc_subnet_ids"], pairs, f"{key_prefix}VpcSubnetIds"
        )
    if "default_auth_scheme" in value:
        pairs.append(
            (f"{key_prefix}DefaultAuthScheme", str(value["default_auth_scheme"]))
        )
    if "auth" in value:
        import capo_rds.types.user_auth_config_info_list

        capo_rds.types.user_auth_config_info_list.serialize_query(
            value["auth"], pairs, f"{key_prefix}Auth"
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "require_tls" in value:
        pairs.append(
            (f"{key_prefix}RequireTLS", "true" if value["require_tls"] else "false")
        )
    if "idle_client_timeout" in value:
        pairs.append(
            (f"{key_prefix}IdleClientTimeout", str(value["idle_client_timeout"]))
        )
    if "debug_logging" in value:
        pairs.append(
            (f"{key_prefix}DebugLogging", "true" if value["debug_logging"] else "false")
        )
    if "created_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["created_date"], pairs, f"{key_prefix}CreatedDate"
        )
    if "updated_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["updated_date"], pairs, f"{key_prefix}UpdatedDate"
        )
    if "endpoint_network_type" in value:
        import capo_rds.types.endpoint_network_type

        capo_rds.types.endpoint_network_type.serialize_query(
            value["endpoint_network_type"], pairs, f"{key_prefix}EndpointNetworkType"
        )
    if "target_connection_network_type" in value:
        import capo_rds.types.target_connection_network_type

        capo_rds.types.target_connection_network_type.serialize_query(
            value["target_connection_network_type"],
            pairs,
            f"{key_prefix}TargetConnectionNetworkType",
        )


def deserialize_query(el: Element) -> DBProxy:
    out: DBProxy = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_db_proxy_arn = el.find("DBProxyArn")
    if child_db_proxy_arn is not None:
        out["db_proxy_arn"] = str(child_db_proxy_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_rds.types.db_proxy_status

        out["status"] = capo_rds.types.db_proxy_status.deserialize_query(child_status)
    child_engine_family = el.find("EngineFamily")
    if child_engine_family is not None:
        out["engine_family"] = str(child_engine_family.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.string_list

        out["vpc_security_group_ids"] = capo_rds.types.string_list.deserialize_query(
            child_vpc_security_group_ids
        )
    child_vpc_subnet_ids = el.find("VpcSubnetIds")
    if child_vpc_subnet_ids is not None:
        import capo_rds.types.string_list

        out["vpc_subnet_ids"] = capo_rds.types.string_list.deserialize_query(
            child_vpc_subnet_ids
        )
    child_default_auth_scheme = el.find("DefaultAuthScheme")
    if child_default_auth_scheme is not None:
        out["default_auth_scheme"] = str(child_default_auth_scheme.text or "")
    child_auth = el.find("Auth")
    if child_auth is not None:
        import capo_rds.types.user_auth_config_info_list

        out["auth"] = capo_rds.types.user_auth_config_info_list.deserialize_query(
            child_auth
        )
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_require_tls = el.find("RequireTLS")
    if child_require_tls is not None:
        out["require_tls"] = (child_require_tls.text or "").lower() == "true"
    child_idle_client_timeout = el.find("IdleClientTimeout")
    if child_idle_client_timeout is not None:
        out["idle_client_timeout"] = int(child_idle_client_timeout.text or "")
    child_debug_logging = el.find("DebugLogging")
    if child_debug_logging is not None:
        out["debug_logging"] = (child_debug_logging.text or "").lower() == "true"
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import capo_rds.types.t_stamp

        out["created_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_created_date
        )
    child_updated_date = el.find("UpdatedDate")
    if child_updated_date is not None:
        import capo_rds.types.t_stamp

        out["updated_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_updated_date
        )
    child_endpoint_network_type = el.find("EndpointNetworkType")
    if child_endpoint_network_type is not None:
        import capo_rds.types.endpoint_network_type

        out["endpoint_network_type"] = (
            capo_rds.types.endpoint_network_type.deserialize_query(
                child_endpoint_network_type
            )
        )
    child_target_connection_network_type = el.find("TargetConnectionNetworkType")
    if child_target_connection_network_type is not None:
        import capo_rds.types.target_connection_network_type

        out["target_connection_network_type"] = (
            capo_rds.types.target_connection_network_type.deserialize_query(
                child_target_connection_network_type
            )
        )
    return out
