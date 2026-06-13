"""Generated from Smithy shape ``com.amazonaws.connectcases#UserUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.custom_entity
    import aws_sdk_connectcases.types.user_arn


class _UserUnion_userArn(TypedDict):
    userArn: "aws_sdk_connectcases.types.user_arn.UserArn"


class _UserUnion_customEntity(TypedDict):
    customEntity: "aws_sdk_connectcases.types.custom_entity.CustomEntity"


UserUnion: TypeAlias = _UserUnion_userArn | _UserUnion_customEntity


# --- restJson1 ser/de ---
def serialize_json(value: UserUnion) -> dict:
    if "userArn" in value:
        return {"userArn": value["userArn"]}
    elif "customEntity" in value:
        return {"customEntity": value["customEntity"]}
    else:
        raise SerializationError("UserUnion: no variant present")


def deserialize_json(data: dict) -> UserUnion:
    if "userArn" in data:
        return {"userArn": data["userArn"]}
    elif "customEntity" in data:
        return {"customEntity": data["customEntity"]}
    else:
        raise DeserializationError("UserUnion: no recognized variant key")
