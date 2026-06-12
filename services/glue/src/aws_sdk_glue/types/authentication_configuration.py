"""Generated from Smithy shape ``com.amazonaws.glue#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.authentication_type
    import aws_sdk_glue.types.kms_key_arn
    import aws_sdk_glue.types.o_auth2_properties
    import aws_sdk_glue.types.secret_arn


class AuthenticationConfiguration(TypedDict):
    authentication_type: NotRequired[
        "aws_sdk_glue.types.authentication_type.AuthenticationType"
    ]
    """<p>A structure containing the authentication configuration.</p>"""
    secret_arn: NotRequired["aws_sdk_glue.types.secret_arn.SecretArn"]
    """<p>The secret manager ARN to store credentials.</p>"""
    kms_key_arn: NotRequired["aws_sdk_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt sensitive authentication information. This key is used to protect credentials and other sensitive data stored within the authentication configuration.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_glue.types.o_auth2_properties.OAuth2Properties"
    ]
    """<p>The properties for OAuth2 authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_glue.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_glue.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "o_auth2_properties" in value:
        import aws_sdk_glue.types.o_auth2_properties

        out["OAuth2Properties"] = (
            aws_sdk_glue.types.o_auth2_properties.serialize_aws_json_1_1(
                value["o_auth2_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_glue.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_glue.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "OAuth2Properties" in data:
        import aws_sdk_glue.types.o_auth2_properties

        out["o_auth2_properties"] = (
            aws_sdk_glue.types.o_auth2_properties.deserialize_aws_json_1_1(
                data["OAuth2Properties"]
            )
        )
    return out
