"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetCredentialsForIdentityInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.arn_string
    import aws_sdk_cognito_identity.types.identity_id
    import aws_sdk_cognito_identity.types.logins_map


class GetCredentialsForIdentityInput(TypedDict):
    identity_id: "aws_sdk_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    logins: NotRequired["aws_sdk_cognito_identity.types.logins_map.LoginsMap"]
    """<p>A set of optional name-value pairs that map provider names to provider tokens. The name-value pair will follow the syntax \"provider_name\": \"provider_user_identifier\".</p> <p>Logins should not be specified when trying to get credentials for an unauthenticated identity.</p> <p>The Logins parameter is required when using identities associated with external identity providers such as Facebook. For examples of <code>Logins</code> maps, see the code examples in the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html\">External Identity Providers</a> section of the Amazon Cognito Developer Guide.</p>"""
    custom_role_arn: NotRequired["aws_sdk_cognito_identity.types.arn_string.ARNString"]
    """<p>The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsForIdentityInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    if "logins" in value:
        import aws_sdk_cognito_identity.types.logins_map

        out["Logins"] = (
            aws_sdk_cognito_identity.types.logins_map.serialize_aws_json_1_1(
                value["logins"]
            )
        )
    if "custom_role_arn" in value:
        out["CustomRoleArn"] = value["custom_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsForIdentityInput:
    out: GetCredentialsForIdentityInput = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    else:
        raise DeserializationError(
            "GetCredentialsForIdentityInput.identity_id required"
        )
    if "Logins" in data:
        import aws_sdk_cognito_identity.types.logins_map

        out["logins"] = (
            aws_sdk_cognito_identity.types.logins_map.deserialize_aws_json_1_1(
                data["Logins"]
            )
        )
    if "CustomRoleArn" in data:
        out["custom_role_arn"] = data["CustomRoleArn"]
    return out
