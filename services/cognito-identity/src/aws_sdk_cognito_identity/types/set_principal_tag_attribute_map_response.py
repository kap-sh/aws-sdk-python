"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#SetPrincipalTagAttributeMapResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_id
    import aws_sdk_cognito_identity.types.identity_provider_name
    import aws_sdk_cognito_identity.types.principal_tags
    import aws_sdk_cognito_identity.types.use_defaults


class SetPrincipalTagAttributeMapResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>The ID of the Identity Pool you want to set attribute mappings for.</p>"""
    identity_provider_name: NotRequired[
        "aws_sdk_cognito_identity.types.identity_provider_name.IdentityProviderName"
    ]
    """<p>The provider name you want to use for attribute mappings.</p>"""
    use_defaults: NotRequired["aws_sdk_cognito_identity.types.use_defaults.UseDefaults"]
    """<p>You can use this operation to select default (username and clientID) attribute mappings.</p>"""
    principal_tags: NotRequired[
        "aws_sdk_cognito_identity.types.principal_tags.PrincipalTags"
    ]
    """<p>You can use this operation to add principal tags. The <code>PrincipalTags</code>operation enables you to reference user attributes in your IAM permissions policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetPrincipalTagAttributeMapResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "identity_provider_name" in value:
        out["IdentityProviderName"] = value["identity_provider_name"]
    if "use_defaults" in value:
        out["UseDefaults"] = value["use_defaults"]
    if "principal_tags" in value:
        import aws_sdk_cognito_identity.types.principal_tags

        out["PrincipalTags"] = (
            aws_sdk_cognito_identity.types.principal_tags.serialize_aws_json_1_1(
                value["principal_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetPrincipalTagAttributeMapResponse:
    out: SetPrincipalTagAttributeMapResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "IdentityProviderName" in data:
        out["identity_provider_name"] = data["IdentityProviderName"]
    if "UseDefaults" in data:
        out["use_defaults"] = data["UseDefaults"]
    if "PrincipalTags" in data:
        import aws_sdk_cognito_identity.types.principal_tags

        out["principal_tags"] = (
            aws_sdk_cognito_identity.types.principal_tags.deserialize_aws_json_1_1(
                data["PrincipalTags"]
            )
        )
    return out
