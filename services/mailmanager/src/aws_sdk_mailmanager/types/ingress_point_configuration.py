"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.secret_arn
    import aws_sdk_mailmanager.types.smtp_password
    import aws_sdk_mailmanager.types.tls_auth_configuration


class _IngressPointConfiguration_SmtpPassword(TypedDict):
    SmtpPassword: "aws_sdk_mailmanager.types.smtp_password.SmtpPassword"


class _IngressPointConfiguration_SecretArn(TypedDict):
    SecretArn: "aws_sdk_mailmanager.types.secret_arn.SecretArn"


class _IngressPointConfiguration_TlsAuthConfiguration(TypedDict):
    TlsAuthConfiguration: (
        "aws_sdk_mailmanager.types.tls_auth_configuration.TlsAuthConfiguration"
    )


IngressPointConfiguration: TypeAlias = (
    _IngressPointConfiguration_SmtpPassword
    | _IngressPointConfiguration_SecretArn
    | _IngressPointConfiguration_TlsAuthConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointConfiguration) -> dict:
    if "SmtpPassword" in value:
        return {"SmtpPassword": value["SmtpPassword"]}
    elif "SecretArn" in value:
        return {"SecretArn": value["SecretArn"]}
    elif "TlsAuthConfiguration" in value:
        import aws_sdk_mailmanager.types.tls_auth_configuration

        return {
            "TlsAuthConfiguration": aws_sdk_mailmanager.types.tls_auth_configuration.serialize_aws_json_1_0(
                value["TlsAuthConfiguration"]
            )
        }
    else:
        raise SerializationError("IngressPointConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressPointConfiguration:
    if "SmtpPassword" in data:
        return {"SmtpPassword": data["SmtpPassword"]}
    elif "SecretArn" in data:
        return {"SecretArn": data["SecretArn"]}
    elif "TlsAuthConfiguration" in data:
        import aws_sdk_mailmanager.types.tls_auth_configuration

        return {
            "TlsAuthConfiguration": aws_sdk_mailmanager.types.tls_auth_configuration.deserialize_aws_json_1_0(
                data["TlsAuthConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "IngressPointConfiguration: no recognized variant key"
        )
