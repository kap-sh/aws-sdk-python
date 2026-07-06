"""Generated from Smithy shape ``com.amazonaws.pipes#SelfManagedKafkaAccessConfigurationCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_pipes.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.secret_manager_arn


class _SelfManagedKafkaAccessConfigurationCredentials_BasicAuth(TypedDict, closed=True):
    BasicAuth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_SaslScram512Auth(
    TypedDict, closed=True
):
    SaslScram512Auth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_SaslScram256Auth(
    TypedDict, closed=True
):
    SaslScram256Auth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_ClientCertificateTlsAuth(
    TypedDict, closed=True
):
    ClientCertificateTlsAuth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


SelfManagedKafkaAccessConfigurationCredentials: TypeAlias = (
    _SelfManagedKafkaAccessConfigurationCredentials_BasicAuth
    | _SelfManagedKafkaAccessConfigurationCredentials_SaslScram512Auth
    | _SelfManagedKafkaAccessConfigurationCredentials_SaslScram256Auth
    | _SelfManagedKafkaAccessConfigurationCredentials_ClientCertificateTlsAuth
)


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedKafkaAccessConfigurationCredentials) -> dict:
    if "BasicAuth" in value:
        return {"BasicAuth": value["BasicAuth"]}
    elif "SaslScram512Auth" in value:
        return {"SaslScram512Auth": value["SaslScram512Auth"]}
    elif "SaslScram256Auth" in value:
        return {"SaslScram256Auth": value["SaslScram256Auth"]}
    elif "ClientCertificateTlsAuth" in value:
        return {"ClientCertificateTlsAuth": value["ClientCertificateTlsAuth"]}
    else:
        raise SerializationError(
            "SelfManagedKafkaAccessConfigurationCredentials: no variant present"
        )


def deserialize_json(data: dict) -> SelfManagedKafkaAccessConfigurationCredentials:
    if "BasicAuth" in data:
        return {"BasicAuth": data["BasicAuth"]}
    elif "SaslScram512Auth" in data:
        return {"SaslScram512Auth": data["SaslScram512Auth"]}
    elif "SaslScram256Auth" in data:
        return {"SaslScram256Auth": data["SaslScram256Auth"]}
    elif "ClientCertificateTlsAuth" in data:
        return {"ClientCertificateTlsAuth": data["ClientCertificateTlsAuth"]}
    else:
        raise DeserializationError(
            "SelfManagedKafkaAccessConfigurationCredentials: no recognized variant key"
        )
