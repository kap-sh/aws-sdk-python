"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.arn
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.db_proxy_name
    import aws_sdk_rds.types.default_auth_scheme
    import aws_sdk_rds.types.endpoint_network_type
    import aws_sdk_rds.types.engine_family
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string_list
    import aws_sdk_rds.types.tag_list
    import aws_sdk_rds.types.target_connection_network_type
    import aws_sdk_rds.types.user_auth_config_list


class CreateDBProxyRequest(TypedDict, closed=True):
    db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The identifier for the proxy. This name must be unique for all proxies owned by your Amazon Web Services account in the specified Amazon Web Services Region. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p>"""
    engine_family: NotRequired["aws_sdk_rds.types.engine_family.EngineFamily"]
    """<p>The kinds of databases that the proxy can connect to. This value determines which database network protocol the proxy recognizes when it interprets network traffic to and from the database. For Aurora MySQL, RDS for MariaDB, and RDS for MySQL databases, specify <code>MYSQL</code>. For Aurora PostgreSQL and RDS for PostgreSQL databases, specify <code>POSTGRESQL</code>. For RDS for Microsoft SQL Server, specify <code>SQLSERVER</code>.</p>"""
    default_auth_scheme: NotRequired[
        "aws_sdk_rds.types.default_auth_scheme.DefaultAuthScheme"
    ]
    """<p>The default authentication scheme that the proxy uses for client connections to the proxy and connections from the proxy to the underlying database. Valid values are <code>NONE</code> and <code>IAM_AUTH</code>. When set to <code>IAM_AUTH</code>, the proxy uses end-to-end IAM authentication to connect to the database. If you don't specify <code>DefaultAuthScheme</code> or specify this parameter as <code>NONE</code>, you must specify the <code>Auth</code> option.</p>"""
    auth: NotRequired["aws_sdk_rds.types.user_auth_config_list.UserAuthConfigList"]
    """<p>The authorization mechanism that the proxy uses.</p>"""
    role_arn: NotRequired["aws_sdk_rds.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in Amazon Web Services Secrets Manager.</p>"""
    vpc_subnet_ids: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>One or more VPC subnet IDs to associate with the new proxy.</p>"""
    vpc_security_group_ids: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>One or more VPC security group IDs to associate with the new proxy.</p>"""
    require_tls: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connections to the proxy.</p>"""
    idle_client_timeout: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it. You can set this value higher or lower than the connection timeout limit for the associated database.</p>"""
    debug_logging: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether the proxy logs detailed connection and query information. When you enable <code>DebugLogging</code>, the proxy captures connection details and connection pool behavior from your queries. Debug logging increases CloudWatch costs and can impact proxy performance. Enable this option only when you need to troubleshoot connection or performance issues.</p>"""
    tags: NotRequired["aws_sdk_rds.types.tag_list.TagList"]
    """<p>An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.</p>"""
    endpoint_network_type: NotRequired[
        "aws_sdk_rds.types.endpoint_network_type.EndpointNetworkType"
    ]
    """<p>The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy endpoint supports IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy endpoint supports IPv6 only.</p> </li> <li> <p> <code>DUAL</code> - The proxy endpoint supports both IPv4 and IPv6.</p> </li> </ul> <p>Default: <code>IPV4</code> </p> <p>Constraints:</p> <ul> <li> <p>If you specify <code>IPV6</code> or <code>DUAL</code>, the VPC and all subnets must have an IPv6 CIDR block.</p> </li> <li> <p>If you specify <code>IPV6</code> or <code>DUAL</code>, the VPC tenancy cannot be <code>dedicated</code>.</p> </li> </ul>"""
    target_connection_network_type: NotRequired[
        "aws_sdk_rds.types.target_connection_network_type.TargetConnectionNetworkType"
    ]
    """<p>The network type that the proxy uses to connect to the target database. The network type determines the IP version that the proxy uses for connections to the database.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> - The proxy connects to the database using IPv4 only.</p> </li> <li> <p> <code>IPV6</code> - The proxy connects to the database using IPv6 only.</p> </li> </ul> <p>Default: <code>IPV4</code> </p> <p>Constraints:</p> <ul> <li> <p>If you specify <code>IPV6</code>, the database must support dual-stack mode. RDS doesn't support IPv6-only databases.</p> </li> <li> <p>All targets registered with the proxy must be compatible with the specified network type.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBProxyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "engine_family" in value:
        import aws_sdk_rds.types.engine_family

        aws_sdk_rds.types.engine_family.serialize_query(
            value["engine_family"], pairs, f"{prefix}.EngineFamily"
        )
    if "default_auth_scheme" in value:
        import aws_sdk_rds.types.default_auth_scheme

        aws_sdk_rds.types.default_auth_scheme.serialize_query(
            value["default_auth_scheme"], pairs, f"{prefix}.DefaultAuthScheme"
        )
    if "auth" in value:
        import aws_sdk_rds.types.user_auth_config_list

        aws_sdk_rds.types.user_auth_config_list.serialize_query(
            value["auth"], pairs, f"{prefix}.Auth"
        )
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "vpc_subnet_ids" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["vpc_subnet_ids"], pairs, f"{prefix}.VpcSubnetIds"
        )
    if "vpc_security_group_ids" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{prefix}.VpcSecurityGroupIds"
        )
    if "require_tls" in value:
        pairs.append(
            (f"{prefix}.RequireTLS", "true" if value["require_tls"] else "false")
        )
    if "idle_client_timeout" in value:
        pairs.append((f"{prefix}.IdleClientTimeout", str(value["idle_client_timeout"])))
    if "debug_logging" in value:
        pairs.append(
            (f"{prefix}.DebugLogging", "true" if value["debug_logging"] else "false")
        )
    if "tags" in value:
        import aws_sdk_rds.types.tag_list

        aws_sdk_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "endpoint_network_type" in value:
        import aws_sdk_rds.types.endpoint_network_type

        aws_sdk_rds.types.endpoint_network_type.serialize_query(
            value["endpoint_network_type"], pairs, f"{prefix}.EndpointNetworkType"
        )
    if "target_connection_network_type" in value:
        import aws_sdk_rds.types.target_connection_network_type

        aws_sdk_rds.types.target_connection_network_type.serialize_query(
            value["target_connection_network_type"],
            pairs,
            f"{prefix}.TargetConnectionNetworkType",
        )


def deserialize_query(el: Element) -> CreateDBProxyRequest:
    out: CreateDBProxyRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_engine_family = el.find("EngineFamily")
    if child_engine_family is not None:
        import aws_sdk_rds.types.engine_family

        out["engine_family"] = aws_sdk_rds.types.engine_family.deserialize_query(
            child_engine_family
        )
    child_default_auth_scheme = el.find("DefaultAuthScheme")
    if child_default_auth_scheme is not None:
        import aws_sdk_rds.types.default_auth_scheme

        out["default_auth_scheme"] = (
            aws_sdk_rds.types.default_auth_scheme.deserialize_query(
                child_default_auth_scheme
            )
        )
    child_auth = el.find("Auth")
    if child_auth is not None:
        import aws_sdk_rds.types.user_auth_config_list

        out["auth"] = aws_sdk_rds.types.user_auth_config_list.deserialize_query(
            child_auth
        )
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_vpc_subnet_ids = el.find("VpcSubnetIds")
    if child_vpc_subnet_ids is not None:
        import aws_sdk_rds.types.string_list

        out["vpc_subnet_ids"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_vpc_subnet_ids
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import aws_sdk_rds.types.string_list

        out["vpc_security_group_ids"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_vpc_security_group_ids
        )
    child_require_tls = el.find("RequireTLS")
    if child_require_tls is not None:
        out["require_tls"] = (child_require_tls.text or "").lower() == "true"
    child_idle_client_timeout = el.find("IdleClientTimeout")
    if child_idle_client_timeout is not None:
        out["idle_client_timeout"] = int(child_idle_client_timeout.text or "")
    child_debug_logging = el.find("DebugLogging")
    if child_debug_logging is not None:
        out["debug_logging"] = (child_debug_logging.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_rds.types.tag_list

        out["tags"] = aws_sdk_rds.types.tag_list.deserialize_query(child_tags)
    child_endpoint_network_type = el.find("EndpointNetworkType")
    if child_endpoint_network_type is not None:
        import aws_sdk_rds.types.endpoint_network_type

        out["endpoint_network_type"] = (
            aws_sdk_rds.types.endpoint_network_type.deserialize_query(
                child_endpoint_network_type
            )
        )
    child_target_connection_network_type = el.find("TargetConnectionNetworkType")
    if child_target_connection_network_type is not None:
        import aws_sdk_rds.types.target_connection_network_type

        out["target_connection_network_type"] = (
            aws_sdk_rds.types.target_connection_network_type.deserialize_query(
                child_target_connection_network_type
            )
        )
    return out
