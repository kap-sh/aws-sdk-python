"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.identity_provider_type


class DescribeIdentityProviderResponse(TypedDict, closed=True):
    identity_provider: "aws_sdk_cognito_identity_provider.types.identity_provider_type.IdentityProviderType"
    """<p>The details of the requested IdP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.identity_provider_type

    out["IdentityProvider"] = (
        aws_sdk_cognito_identity_provider.types.identity_provider_type.serialize_aws_json_1_1(
            value["identity_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityProviderResponse:
    out: DescribeIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_cognito_identity_provider.types.identity_provider_type

        out["identity_provider"] = (
            aws_sdk_cognito_identity_provider.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeIdentityProviderResponse.identity_provider required"
        )
    return out
