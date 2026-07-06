"""Generated from Smithy shape ``com.amazonaws.quicksight#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.identity_type
    import aws_sdk_quicksight.types.role_name
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user_name
    import aws_sdk_quicksight.types.user_role


class User(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the user.</p>"""
    user_name: NotRequired["aws_sdk_quicksight.types.user_name.UserName"]
    """<p>The user's user name. This value is required if you are registering a user that will be managed in Quick Sight. In the output, the value for <code>UserName</code> is <code>N/A</code> when the value for <code>IdentityType</code> is <code>IAM</code> and the corresponding IAM user is deleted.</p>"""
    email: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The user's email address.</p>"""
    role: NotRequired["aws_sdk_quicksight.types.user_role.UserRole"]
    """<p>The Quick Sight role for the user. The user role can be one of the following:.</p> <ul> <li> <p> <code>READER</code>: A user who has read-only access to dashboards.</p> </li> <li> <p> <code>AUTHOR</code>: A user who can create data sources, datasets, analyses, and dashboards.</p> </li> <li> <p> <code>ADMIN</code>: A user who is an author, who can also manage Amazon Quick Sight settings.</p> </li> <li> <p> <code>READER_PRO</code>: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.</p> </li> <li> <p> <code>AUTHOR_PRO</code>: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.</p> </li> <li> <p> <code>ADMIN_PRO</code>: Admin Pros are Author Pros who can also manage Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.</p> </li> <li> <p> <code>RESTRICTED_READER</code>: This role isn't currently available for use.</p> </li> <li> <p> <code>RESTRICTED_AUTHOR</code>: This role isn't currently available for use.</p> </li> </ul>"""
    identity_type: NotRequired["aws_sdk_quicksight.types.identity_type.IdentityType"]
    """<p>The type of identity authentication used by the user.</p>"""
    active: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The active status of user. When you create an Quick Sight user that's not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.</p>"""
    principal_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The principal ID of the user.</p>"""
    custom_permissions_name: NotRequired["aws_sdk_quicksight.types.role_name.RoleName"]
    """<p>The custom permissions profile associated with this user.</p>"""
    external_login_federation_provider_type: NotRequired[
        "aws_sdk_quicksight.types.string.String"
    ]
    """<p>The type of supported external login provider that provides identity to let the user federate into Quick Sight with an associated IAM role. The type can be one of the following.</p> <ul> <li> <p> <code>COGNITO</code>: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com.</p> </li> <li> <p> <code>CUSTOM_OIDC</code>: Custom OpenID Connect (OIDC) provider.</p> </li> </ul>"""
    external_login_federation_provider_url: NotRequired[
        "aws_sdk_quicksight.types.string.String"
    ]
    """<p>The URL of the external login provider.</p>"""
    external_login_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The identity ID for the user in the external login provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "email" in value:
        out["Email"] = value["email"]
    if "role" in value:
        import aws_sdk_quicksight.types.user_role

        out["Role"] = aws_sdk_quicksight.types.user_role.serialize_json(value["role"])
    if "identity_type" in value:
        import aws_sdk_quicksight.types.identity_type

        out["IdentityType"] = aws_sdk_quicksight.types.identity_type.serialize_json(
            value["identity_type"]
        )
    out["Active"] = value.get("active", False)
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "custom_permissions_name" in value:
        out["CustomPermissionsName"] = value["custom_permissions_name"]
    if "external_login_federation_provider_type" in value:
        out["ExternalLoginFederationProviderType"] = value[
            "external_login_federation_provider_type"
        ]
    if "external_login_federation_provider_url" in value:
        out["ExternalLoginFederationProviderUrl"] = value[
            "external_login_federation_provider_url"
        ]
    if "external_login_id" in value:
        out["ExternalLoginId"] = value["external_login_id"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Role" in data:
        import aws_sdk_quicksight.types.user_role

        out["role"] = aws_sdk_quicksight.types.user_role.deserialize_json(data["Role"])
    if "IdentityType" in data:
        import aws_sdk_quicksight.types.identity_type

        out["identity_type"] = aws_sdk_quicksight.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if "Active" in data:
        out["active"] = data["Active"]
    else:
        out["active"] = False
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    if "ExternalLoginFederationProviderType" in data:
        out["external_login_federation_provider_type"] = data[
            "ExternalLoginFederationProviderType"
        ]
    if "ExternalLoginFederationProviderUrl" in data:
        out["external_login_federation_provider_url"] = data[
            "ExternalLoginFederationProviderUrl"
        ]
    if "ExternalLoginId" in data:
        out["external_login_id"] = data["ExternalLoginId"]
    return out
