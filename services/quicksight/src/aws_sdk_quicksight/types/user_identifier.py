"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.sensitive_string


class _UserIdentifier_UserName(TypedDict, closed=True):
    UserName: "aws_sdk_quicksight.types.sensitive_string.SensitiveString"


class _UserIdentifier_Email(TypedDict, closed=True):
    Email: "aws_sdk_quicksight.types.sensitive_string.SensitiveString"


class _UserIdentifier_UserArn(TypedDict, closed=True):
    UserArn: "aws_sdk_quicksight.types.arn.Arn"


UserIdentifier: TypeAlias = (
    _UserIdentifier_UserName | _UserIdentifier_Email | _UserIdentifier_UserArn
)


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentifier) -> dict:
    if "UserName" in value:
        return {"UserName": value["UserName"]}
    elif "Email" in value:
        return {"Email": value["Email"]}
    elif "UserArn" in value:
        return {"UserArn": value["UserArn"]}
    else:
        raise SerializationError("UserIdentifier: no variant present")


def deserialize_json(data: dict) -> UserIdentifier:
    if "UserName" in data:
        return {"UserName": data["UserName"]}
    elif "Email" in data:
        return {"Email": data["Email"]}
    elif "UserArn" in data:
        return {"UserArn": data["UserArn"]}
    else:
        raise DeserializationError("UserIdentifier: no recognized variant key")
