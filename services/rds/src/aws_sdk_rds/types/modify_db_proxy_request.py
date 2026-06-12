"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.arn
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.db_proxy_name
    import aws_sdk_rds.types.default_auth_scheme
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string_list
    import aws_sdk_rds.types.user_auth_config_list


class ModifyDBProxyRequest(TypedDict):
    db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The identifier for the <code>DBProxy</code> to modify.</p>"""
    new_db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The new identifier for the <code>DBProxy</code>. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p>"""
    default_auth_scheme: NotRequired[
        "aws_sdk_rds.types.default_auth_scheme.DefaultAuthScheme"
    ]
    """<p>The default authentication scheme that the proxy uses for client connections to the proxy and connections from the proxy to the underlying database. Valid values are <code>NONE</code> and <code>IAM_AUTH</code>. When set to <code>IAM_AUTH</code>, the proxy uses end-to-end IAM authentication to connect to the database.</p>"""
    auth: NotRequired["aws_sdk_rds.types.user_auth_config_list.UserAuthConfigList"]
    """<p>The new authentication settings for the <code>DBProxy</code>.</p>"""
    require_tls: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Whether Transport Layer Security (TLS) encryption is required for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connections to the proxy, even if the associated database doesn't use TLS.</p>"""
    idle_client_timeout: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it. You can set this value higher or lower than the connection timeout limit for the associated database.</p>"""
    debug_logging: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the proxy logs detailed connection and query information. When you enable <code>DebugLogging</code>, the proxy captures connection details and connection pool behavior from your queries. Debug logging increases CloudWatch costs and can impact proxy performance. Enable this option only when you need to troubleshoot connection or performance issues.</p>"""
    role_arn: NotRequired["aws_sdk_rds.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in Amazon Web Services Secrets Manager.</p>"""
    security_groups: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>The new list of security groups for the <code>DBProxy</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "new_db_proxy_name" in value:
        pairs.append((f"{prefix}.NewDBProxyName", str(value["new_db_proxy_name"])))
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
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "security_groups" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroups"
        )


def deserialize_query(el: Element) -> ModifyDBProxyRequest:
    out: ModifyDBProxyRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_new_db_proxy_name = el.find("NewDBProxyName")
    if child_new_db_proxy_name is not None:
        out["new_db_proxy_name"] = str(child_new_db_proxy_name.text or "")
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
    child_require_tls = el.find("RequireTLS")
    if child_require_tls is not None:
        out["require_tls"] = (child_require_tls.text or "").lower() == "true"
    child_idle_client_timeout = el.find("IdleClientTimeout")
    if child_idle_client_timeout is not None:
        out["idle_client_timeout"] = int(child_idle_client_timeout.text or "")
    child_debug_logging = el.find("DebugLogging")
    if child_debug_logging is not None:
        out["debug_logging"] = (child_debug_logging.text or "").lower() == "true"
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import aws_sdk_rds.types.string_list

        out["security_groups"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_security_groups
        )
    return out
