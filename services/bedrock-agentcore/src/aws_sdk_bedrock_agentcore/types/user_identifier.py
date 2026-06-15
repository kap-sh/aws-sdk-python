"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.user_id_type
    import aws_sdk_bedrock_agentcore.types.user_token_type


class _UserIdentifier_userToken(TypedDict):
    userToken: "aws_sdk_bedrock_agentcore.types.user_token_type.UserTokenType"


class _UserIdentifier_userId(TypedDict):
    userId: "aws_sdk_bedrock_agentcore.types.user_id_type.UserIdType"


UserIdentifier: TypeAlias = _UserIdentifier_userToken | _UserIdentifier_userId


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentifier) -> dict:
    if "userToken" in value:
        return {"userToken": value["userToken"]}
    elif "userId" in value:
        return {"userId": value["userId"]}
    else:
        raise SerializationError("UserIdentifier: no variant present")


def deserialize_json(data: dict) -> UserIdentifier:
    if "userToken" in data:
        return {"userToken": data["userToken"]}
    elif "userId" in data:
        return {"userId": data["userId"]}
    else:
        raise DeserializationError("UserIdentifier: no recognized variant key")
