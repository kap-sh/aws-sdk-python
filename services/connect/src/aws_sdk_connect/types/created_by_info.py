"""Generated from Smithy shape ``com.amazonaws.connect#CreatedByInfo``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn


class _CreatedByInfo_ConnectUserArn(TypedDict):
    ConnectUserArn: "aws_sdk_connect.types.arn.ARN"


class _CreatedByInfo_AWSIdentityArn(TypedDict):
    AWSIdentityArn: "aws_sdk_connect.types.arn.ARN"


CreatedByInfo: TypeAlias = _CreatedByInfo_ConnectUserArn | _CreatedByInfo_AWSIdentityArn


# --- restJson1 ser/de ---
def serialize_json(value: CreatedByInfo) -> dict:
    if "ConnectUserArn" in value:
        return {"ConnectUserArn": value["ConnectUserArn"]}
    elif "AWSIdentityArn" in value:
        return {"AWSIdentityArn": value["AWSIdentityArn"]}
    else:
        raise SerializationError("CreatedByInfo: no variant present")


def deserialize_json(data: dict) -> CreatedByInfo:
    if "ConnectUserArn" in data:
        return {"ConnectUserArn": data["ConnectUserArn"]}
    elif "AWSIdentityArn" in data:
        return {"AWSIdentityArn": data["AWSIdentityArn"]}
    else:
        raise DeserializationError("CreatedByInfo: no recognized variant key")
