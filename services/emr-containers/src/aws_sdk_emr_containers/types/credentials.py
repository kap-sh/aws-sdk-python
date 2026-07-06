"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Credentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_emr_containers.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.token


class _Credentials_token(TypedDict, closed=True):
    token: "aws_sdk_emr_containers.types.token.Token"


Credentials: TypeAlias = _Credentials_token


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    if "token" in value:
        return {"token": value["token"]}
    else:
        raise SerializationError("Credentials: no variant present")


def deserialize_json(data: dict) -> Credentials:
    if "token" in data:
        return {"token": data["token"]}
    else:
        raise DeserializationError("Credentials: no recognized variant key")
