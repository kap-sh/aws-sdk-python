"""Generated from Smithy shape ``com.amazonaws.pipes#MQBrokerAccessCredentials``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_pipes.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.secret_manager_arn


class _MQBrokerAccessCredentials_BasicAuth(TypedDict):
    BasicAuth: "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"


MQBrokerAccessCredentials: TypeAlias = _MQBrokerAccessCredentials_BasicAuth


# --- restJson1 ser/de ---
def serialize_json(value: MQBrokerAccessCredentials) -> dict:
    if "BasicAuth" in value:
        return {"BasicAuth": value["BasicAuth"]}
    else:
        raise SerializationError("MQBrokerAccessCredentials: no variant present")


def deserialize_json(data: dict) -> MQBrokerAccessCredentials:
    if "BasicAuth" in data:
        return {"BasicAuth": data["BasicAuth"]}
    else:
        raise DeserializationError(
            "MQBrokerAccessCredentials: no recognized variant key"
        )
