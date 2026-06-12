"""Generated from Smithy shape ``com.amazonaws.pipes#MSKAccessCredentials``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_pipes.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.secret_manager_arn


class _MSKAccessCredentials_SaslScram512Auth(TypedDict):
    SaslScram512Auth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


class _MSKAccessCredentials_ClientCertificateTlsAuth(TypedDict):
    ClientCertificateTlsAuth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


MSKAccessCredentials: TypeAlias = (
    _MSKAccessCredentials_SaslScram512Auth
    | _MSKAccessCredentials_ClientCertificateTlsAuth
)


# --- restJson1 ser/de ---
def serialize_json(value: MSKAccessCredentials) -> dict:
    if "SaslScram512Auth" in value:
        return {"SaslScram512Auth": value["SaslScram512Auth"]}
    elif "ClientCertificateTlsAuth" in value:
        return {"ClientCertificateTlsAuth": value["ClientCertificateTlsAuth"]}
    else:
        raise SerializationError("MSKAccessCredentials: no variant present")


def deserialize_json(data: dict) -> MSKAccessCredentials:
    if "SaslScram512Auth" in data:
        return {"SaslScram512Auth": data["SaslScram512Auth"]}
    elif "ClientCertificateTlsAuth" in data:
        return {"ClientCertificateTlsAuth": data["ClientCertificateTlsAuth"]}
    else:
        raise DeserializationError("MSKAccessCredentials: no recognized variant key")
