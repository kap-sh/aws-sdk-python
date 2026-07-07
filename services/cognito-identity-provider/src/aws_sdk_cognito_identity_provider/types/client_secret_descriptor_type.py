"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientSecretDescriptorType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_secret_id_type
    import aws_sdk_cognito_identity_provider.types.client_secret_type
    import aws_sdk_cognito_identity_provider.types.date_type


class ClientSecretDescriptorType(TypedDict, closed=True):
    client_secret_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_id_type.ClientSecretIdType"
    ]
    """<p>The unique identifier for the client secret. This identifier follows the format <client-id>--<epoch-create-time>.</p>"""
    client_secret_value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The actual secret value. This is only returned when creating a new secret and only if Amazon Cognito generated the secret. For custom secrets that you provide, this field is not included in the response.</p>"""
    client_secret_create_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the client secret was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSecretDescriptorType) -> dict:
    out: dict = {}
    if "client_secret_id" in value:
        out["ClientSecretId"] = value["client_secret_id"]
    if "client_secret_value" in value:
        out["ClientSecretValue"] = value["client_secret_value"]
    if "client_secret_create_date" in value:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["ClientSecretCreateDate"] = (
            aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["client_secret_create_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientSecretDescriptorType:
    out: ClientSecretDescriptorType = {}  # type: ignore[typeddict-item]
    if "ClientSecretId" in data:
        out["client_secret_id"] = data["ClientSecretId"]
    if "ClientSecretValue" in data:
        out["client_secret_value"] = data["ClientSecretValue"]
    if "ClientSecretCreateDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["client_secret_create_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["ClientSecretCreateDate"]
            )
        )
    return out
