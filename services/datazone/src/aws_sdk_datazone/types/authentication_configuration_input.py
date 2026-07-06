"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authentication_type
    import aws_sdk_datazone.types.basic_authentication_credentials
    import aws_sdk_datazone.types.credential_map
    import aws_sdk_datazone.types.o_auth2_properties


class AuthenticationConfigurationInput(TypedDict, closed=True):
    authentication_type: NotRequired[
        "aws_sdk_datazone.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type of a connection.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_datazone.types.o_auth2_properties.OAuth2Properties"
    ]
    """<p>The oAuth2 properties of a connection.</p>"""
    secret_arn: NotRequired["str"]
    """<p>The secret ARN of a connection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The KMS key ARN of a connection.</p>"""
    basic_authentication_credentials: NotRequired[
        "aws_sdk_datazone.types.basic_authentication_credentials.BasicAuthenticationCredentials"
    ]
    """<p>The basic authentication credentials of a connection.</p>"""
    custom_authentication_credentials: NotRequired[
        "aws_sdk_datazone.types.credential_map.CredentialMap"
    ]
    """<p>The custom authentication credentials of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfigurationInput) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_datazone.types.authentication_type

        out["authenticationType"] = (
            aws_sdk_datazone.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "o_auth2_properties" in value:
        import aws_sdk_datazone.types.o_auth2_properties

        out["oAuth2Properties"] = (
            aws_sdk_datazone.types.o_auth2_properties.serialize_json(
                value["o_auth2_properties"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "basic_authentication_credentials" in value:
        import aws_sdk_datazone.types.basic_authentication_credentials

        out["basicAuthenticationCredentials"] = (
            aws_sdk_datazone.types.basic_authentication_credentials.serialize_json(
                value["basic_authentication_credentials"]
            )
        )
    if "custom_authentication_credentials" in value:
        import aws_sdk_datazone.types.credential_map

        out["customAuthenticationCredentials"] = (
            aws_sdk_datazone.types.credential_map.serialize_json(
                value["custom_authentication_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfigurationInput:
    out: AuthenticationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "authenticationType" in data:
        import aws_sdk_datazone.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_datazone.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if "oAuth2Properties" in data:
        import aws_sdk_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            aws_sdk_datazone.types.o_auth2_properties.deserialize_json(
                data["oAuth2Properties"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "basicAuthenticationCredentials" in data:
        import aws_sdk_datazone.types.basic_authentication_credentials

        out["basic_authentication_credentials"] = (
            aws_sdk_datazone.types.basic_authentication_credentials.deserialize_json(
                data["basicAuthenticationCredentials"]
            )
        )
    if "customAuthenticationCredentials" in data:
        import aws_sdk_datazone.types.credential_map

        out["custom_authentication_credentials"] = (
            aws_sdk_datazone.types.credential_map.deserialize_json(
                data["customAuthenticationCredentials"]
            )
        )
    return out
