"""Generated from Smithy shape ``com.amazonaws.rds#UserAuthConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.arn
    import aws_sdk_rds.types.auth_scheme
    import aws_sdk_rds.types.auth_user_name
    import aws_sdk_rds.types.client_password_auth_type
    import aws_sdk_rds.types.description
    import aws_sdk_rds.types.iam_auth_mode


class UserAuthConfig(TypedDict):
    description: NotRequired["aws_sdk_rds.types.description.Description"]
    """<p>A user-specified description about the authentication used by a proxy to log in as a specific database user.</p>"""
    user_name: NotRequired["aws_sdk_rds.types.auth_user_name.AuthUserName"]
    """<p>The name of the database user to which the proxy connects.</p>"""
    auth_scheme: NotRequired["aws_sdk_rds.types.auth_scheme.AuthScheme"]
    """<p>The type of authentication that the proxy uses for connections from the proxy to the underlying database.</p>"""
    secret_arn: NotRequired["aws_sdk_rds.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.</p>"""
    iam_auth: NotRequired["aws_sdk_rds.types.iam_auth_mode.IAMAuthMode"]
    """<p>A value that indicates whether to require or disallow Amazon Web Services Identity and Access Management (IAM) authentication for connections to the proxy. The <code>ENABLED</code> value is valid only for proxies with RDS for Microsoft SQL Server.</p>"""
    client_password_auth_type: NotRequired[
        "aws_sdk_rds.types.client_password_auth_type.ClientPasswordAuthType"
    ]
    """<p>The type of authentication the proxy uses for connections from clients. The following values are defaults for the corresponding engines:</p> <ul> <li> <p>RDS for MySQL: <code>MYSQL_CACHING_SHA2_PASSWORD</code> </p> </li> <li> <p>RDS for SQL Server: <code>SQL_SERVER_AUTHENTICATION</code> </p> </li> <li> <p>RDS for PostgreSQL: <code>POSTGRES_SCRAM_SHA2_256</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserAuthConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    if "auth_scheme" in value:
        import aws_sdk_rds.types.auth_scheme

        aws_sdk_rds.types.auth_scheme.serialize_query(
            value["auth_scheme"], pairs, f"{prefix}.AuthScheme"
        )
    if "secret_arn" in value:
        pairs.append((f"{prefix}.SecretArn", str(value["secret_arn"])))
    if "iam_auth" in value:
        import aws_sdk_rds.types.iam_auth_mode

        aws_sdk_rds.types.iam_auth_mode.serialize_query(
            value["iam_auth"], pairs, f"{prefix}.IAMAuth"
        )
    if "client_password_auth_type" in value:
        import aws_sdk_rds.types.client_password_auth_type

        aws_sdk_rds.types.client_password_auth_type.serialize_query(
            value["client_password_auth_type"],
            pairs,
            f"{prefix}.ClientPasswordAuthType",
        )


def deserialize_query(el: Element) -> UserAuthConfig:
    out: UserAuthConfig = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_auth_scheme = el.find("AuthScheme")
    if child_auth_scheme is not None:
        import aws_sdk_rds.types.auth_scheme

        out["auth_scheme"] = aws_sdk_rds.types.auth_scheme.deserialize_query(
            child_auth_scheme
        )
    child_secret_arn = el.find("SecretArn")
    if child_secret_arn is not None:
        out["secret_arn"] = str(child_secret_arn.text or "")
    child_iam_auth = el.find("IAMAuth")
    if child_iam_auth is not None:
        import aws_sdk_rds.types.iam_auth_mode

        out["iam_auth"] = aws_sdk_rds.types.iam_auth_mode.deserialize_query(
            child_iam_auth
        )
    child_client_password_auth_type = el.find("ClientPasswordAuthType")
    if child_client_password_auth_type is not None:
        import aws_sdk_rds.types.client_password_auth_type

        out["client_password_auth_type"] = (
            aws_sdk_rds.types.client_password_auth_type.deserialize_query(
                child_client_password_auth_type
            )
        )
    return out
