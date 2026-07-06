"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.identity_provider_type


class UpdateIdentityProviderResponse(TypedDict, closed=True):
    identity_provider: "aws_sdk_cognito_identity_provider.types.identity_provider_type.IdentityProviderType"
    """<p>The identity provider details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIdentityProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.identity_provider_type

    out["IdentityProvider"] = (
        aws_sdk_cognito_identity_provider.types.identity_provider_type.serialize_aws_json_1_1(
            value["identity_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIdentityProviderResponse:
    out: UpdateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_cognito_identity_provider.types.identity_provider_type

        out["identity_provider"] = (
            aws_sdk_cognito_identity_provider.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdentityProviderResponse.identity_provider required"
        )
    return out
