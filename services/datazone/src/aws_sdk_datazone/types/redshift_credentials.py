"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftCredentials``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.username_password


class _RedshiftCredentials_secretArn(TypedDict):
    secretArn: "str"


class _RedshiftCredentials_usernamePassword(TypedDict):
    usernamePassword: "aws_sdk_datazone.types.username_password.UsernamePassword"


RedshiftCredentials: TypeAlias = (
    _RedshiftCredentials_secretArn | _RedshiftCredentials_usernamePassword
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftCredentials) -> dict:
    if "secretArn" in value:
        return {"secretArn": value["secretArn"]}
    elif "usernamePassword" in value:
        import aws_sdk_datazone.types.username_password

        return {
            "usernamePassword": aws_sdk_datazone.types.username_password.serialize_json(
                value["usernamePassword"]
            )
        }
    else:
        raise SerializationError("RedshiftCredentials: no variant present")


def deserialize_json(data: dict) -> RedshiftCredentials:
    if "secretArn" in data:
        return {"secretArn": data["secretArn"]}
    elif "usernamePassword" in data:
        import aws_sdk_datazone.types.username_password

        return {
            "usernamePassword": aws_sdk_datazone.types.username_password.deserialize_json(
                data["usernamePassword"]
            )
        }
    else:
        raise DeserializationError("RedshiftCredentials: no recognized variant key")
