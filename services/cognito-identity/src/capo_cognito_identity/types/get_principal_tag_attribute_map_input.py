"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetPrincipalTagAttributeMapInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.identity_provider_name


class GetPrincipalTagAttributeMapInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>You can use this operation to get the ID of the Identity Pool you setup attribute mappings for.</p>"""
    identity_provider_name: (
        "capo_cognito_identity.types.identity_provider_name.IdentityProviderName"
    )
    """<p>You can use this operation to get the provider name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPrincipalTagAttributeMapInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    out["IdentityProviderName"] = value["identity_provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPrincipalTagAttributeMapInput:
    out: GetPrincipalTagAttributeMapInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "GetPrincipalTagAttributeMapInput.identity_pool_id required"
        )
    if "IdentityProviderName" in data:
        out["identity_provider_name"] = data["IdentityProviderName"]
    else:
        raise DeserializationError(
            "GetPrincipalTagAttributeMapInput.identity_provider_name required"
        )
    return out
