"""Generated from Smithy shape ``com.amazonaws.rds#UserAuthConfigInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.auth_scheme
    import capo_rds.types.client_password_auth_type
    import capo_rds.types.iam_auth_mode
    import capo_rds.types.string


class UserAuthConfigInfo(TypedDict, closed=True):
    description: NotRequired["capo_rds.types.string.String"]
    """<p>A user-specified description about the authentication used by a proxy to log in as a specific database user.</p>"""
    user_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database user to which the proxy connects.</p>"""
    auth_scheme: NotRequired["capo_rds.types.auth_scheme.AuthScheme"]
    """<p>The type of authentication that the proxy uses for connections from the proxy to the underlying database.</p>"""
    secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.</p>"""
    iam_auth: NotRequired["capo_rds.types.iam_auth_mode.IAMAuthMode"]
    """<p>Whether to require or disallow Amazon Web Services Identity and Access Management (IAM) authentication for connections to the proxy. </p>"""
    client_password_auth_type: NotRequired[
        "capo_rds.types.client_password_auth_type.ClientPasswordAuthType"
    ]
    """<p>The type of authentication the proxy uses for connections from clients.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserAuthConfigInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "auth_scheme" in value:
        import capo_rds.types.auth_scheme

        capo_rds.types.auth_scheme.serialize_query(
            value["auth_scheme"], pairs, f"{key_prefix}AuthScheme"
        )
    if "secret_arn" in value:
        pairs.append((f"{key_prefix}SecretArn", str(value["secret_arn"])))
    if "iam_auth" in value:
        import capo_rds.types.iam_auth_mode

        capo_rds.types.iam_auth_mode.serialize_query(
            value["iam_auth"], pairs, f"{key_prefix}IAMAuth"
        )
    if "client_password_auth_type" in value:
        import capo_rds.types.client_password_auth_type

        capo_rds.types.client_password_auth_type.serialize_query(
            value["client_password_auth_type"],
            pairs,
            f"{key_prefix}ClientPasswordAuthType",
        )


def deserialize_query(el: Element) -> UserAuthConfigInfo:
    out: UserAuthConfigInfo = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_auth_scheme = el.find("AuthScheme")
    if child_auth_scheme is not None:
        import capo_rds.types.auth_scheme

        out["auth_scheme"] = capo_rds.types.auth_scheme.deserialize_query(
            child_auth_scheme
        )
    child_secret_arn = el.find("SecretArn")
    if child_secret_arn is not None:
        out["secret_arn"] = str(child_secret_arn.text or "")
    child_iam_auth = el.find("IAMAuth")
    if child_iam_auth is not None:
        import capo_rds.types.iam_auth_mode

        out["iam_auth"] = capo_rds.types.iam_auth_mode.deserialize_query(child_iam_auth)
    child_client_password_auth_type = el.find("ClientPasswordAuthType")
    if child_client_password_auth_type is not None:
        import capo_rds.types.client_password_auth_type

        out["client_password_auth_type"] = (
            capo_rds.types.client_password_auth_type.deserialize_query(
                child_client_password_auth_type
            )
        )
    return out
