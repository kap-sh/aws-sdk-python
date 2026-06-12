"""Generated from Smithy shape ``com.amazonaws.sso#GetRoleCredentialsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso.types.access_token_type
    import aws_sdk_sso.types.account_id_type
    import aws_sdk_sso.types.role_name_type


class GetRoleCredentialsRequest(TypedDict):
    role_name: "aws_sdk_sso.types.role_name_type.RoleNameType"
    """<p>The friendly name of the role that is assigned to the user.</p>"""
    account_id: "aws_sdk_sso.types.account_id_type.AccountIdType"
    """<p>The identifier for the AWS account that is assigned to the user.</p>"""
    access_token: "aws_sdk_sso.types.access_token_type.AccessTokenType"
    """<p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoleCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRoleCredentialsRequest:
    out: GetRoleCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
