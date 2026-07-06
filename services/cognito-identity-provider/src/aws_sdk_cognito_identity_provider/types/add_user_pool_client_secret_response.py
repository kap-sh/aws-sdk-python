"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AddUserPoolClientSecretResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type


class AddUserPoolClientSecretResponse(TypedDict, closed=True):
    client_secret_descriptor: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.ClientSecretDescriptorType"
    ]
    """<p>The details of the newly created client secret, including its unique identifier and creation timestamp. The ClientSecretValue is only returned when Amazon Cognito generates the secret. For custom secrets that you provide, the ClientSecretValue is not included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddUserPoolClientSecretResponse) -> dict:
    out: dict = {}
    if "client_secret_descriptor" in value:
        import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type

        out["ClientSecretDescriptor"] = (
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.serialize_aws_json_1_1(
                value["client_secret_descriptor"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddUserPoolClientSecretResponse:
    out: AddUserPoolClientSecretResponse = {}  # type: ignore[typeddict-item]
    if "ClientSecretDescriptor" in data:
        import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type

        out["client_secret_descriptor"] = (
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.deserialize_aws_json_1_1(
                data["ClientSecretDescriptor"]
            )
        )
    return out
