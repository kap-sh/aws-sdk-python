"""Generated from Smithy shape ``com.amazonaws.glue#AuthenticationConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.authentication_type
    import aws_sdk_glue.types.basic_authentication_credentials
    import aws_sdk_glue.types.credential_map
    import aws_sdk_glue.types.kms_key_arn
    import aws_sdk_glue.types.o_auth2_properties_input
    import aws_sdk_glue.types.secret_arn


class AuthenticationConfigurationInput(TypedDict):
    authentication_type: NotRequired[
        "aws_sdk_glue.types.authentication_type.AuthenticationType"
    ]
    """<p>A structure containing the authentication configuration in the CreateConnection request.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_glue.types.o_auth2_properties_input.OAuth2PropertiesInput"
    ]
    """<p>The properties for OAuth2 authentication in the CreateConnection request.</p>"""
    secret_arn: NotRequired["aws_sdk_glue.types.secret_arn.SecretArn"]
    """<p>The secret manager ARN to store credentials in the CreateConnection request.</p>"""
    kms_key_arn: NotRequired["aws_sdk_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt the connection. Only taken an as input in the request and stored in the Secret Manager.</p>"""
    basic_authentication_credentials: NotRequired[
        "aws_sdk_glue.types.basic_authentication_credentials.BasicAuthenticationCredentials"
    ]
    """<p>The credentials used when the authentication type is basic authentication.</p>"""
    custom_authentication_credentials: NotRequired[
        "aws_sdk_glue.types.credential_map.CredentialMap"
    ]
    """<p>The credentials used when the authentication type is custom authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationConfigurationInput) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_glue.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_glue.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "o_auth2_properties" in value:
        import aws_sdk_glue.types.o_auth2_properties_input

        out["OAuth2Properties"] = (
            aws_sdk_glue.types.o_auth2_properties_input.serialize_aws_json_1_1(
                value["o_auth2_properties"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "basic_authentication_credentials" in value:
        import aws_sdk_glue.types.basic_authentication_credentials

        out["BasicAuthenticationCredentials"] = (
            aws_sdk_glue.types.basic_authentication_credentials.serialize_aws_json_1_1(
                value["basic_authentication_credentials"]
            )
        )
    if "custom_authentication_credentials" in value:
        import aws_sdk_glue.types.credential_map

        out["CustomAuthenticationCredentials"] = (
            aws_sdk_glue.types.credential_map.serialize_aws_json_1_1(
                value["custom_authentication_credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationConfigurationInput:
    out: AuthenticationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_glue.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_glue.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "OAuth2Properties" in data:
        import aws_sdk_glue.types.o_auth2_properties_input

        out["o_auth2_properties"] = (
            aws_sdk_glue.types.o_auth2_properties_input.deserialize_aws_json_1_1(
                data["OAuth2Properties"]
            )
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "BasicAuthenticationCredentials" in data:
        import aws_sdk_glue.types.basic_authentication_credentials

        out["basic_authentication_credentials"] = (
            aws_sdk_glue.types.basic_authentication_credentials.deserialize_aws_json_1_1(
                data["BasicAuthenticationCredentials"]
            )
        )
    if "CustomAuthenticationCredentials" in data:
        import aws_sdk_glue.types.credential_map

        out["custom_authentication_credentials"] = (
            aws_sdk_glue.types.credential_map.deserialize_aws_json_1_1(
                data["CustomAuthenticationCredentials"]
            )
        )
    return out
