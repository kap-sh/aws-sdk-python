"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#SetPrincipalTagAttributeMapInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_id
    import aws_sdk_cognito_identity.types.identity_provider_name
    import aws_sdk_cognito_identity.types.principal_tags
    import aws_sdk_cognito_identity.types.use_defaults


class SetPrincipalTagAttributeMapInput(TypedDict):
    identity_pool_id: "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>The ID of the Identity Pool you want to set attribute mappings for.</p>"""
    identity_provider_name: (
        "aws_sdk_cognito_identity.types.identity_provider_name.IdentityProviderName"
    )
    """<p>The provider name you want to use for attribute mappings.</p>"""
    use_defaults: NotRequired["aws_sdk_cognito_identity.types.use_defaults.UseDefaults"]
    """<p>You can use this operation to use default (username and clientID) attribute mappings.</p>"""
    principal_tags: NotRequired[
        "aws_sdk_cognito_identity.types.principal_tags.PrincipalTags"
    ]
    """<p>You can use this operation to add principal tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetPrincipalTagAttributeMapInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
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


def deserialize_aws_json_1_1(data: dict) -> SetPrincipalTagAttributeMapInput:
    out: SetPrincipalTagAttributeMapInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "SetPrincipalTagAttributeMapInput.identity_pool_id required"
        )
    if "IdentityProviderName" in data:
        out["identity_provider_name"] = data["IdentityProviderName"]
    else:
        raise DeserializationError(
            "SetPrincipalTagAttributeMapInput.identity_provider_name required"
        )
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
