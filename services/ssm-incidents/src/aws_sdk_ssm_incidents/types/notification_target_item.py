"""Generated from Smithy shape ``com.amazonaws.ssmincidents#NotificationTargetItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class _NotificationTargetItem_snsTopicArn(TypedDict):
    snsTopicArn: "aws_sdk_ssm_incidents.types.arn.Arn"


NotificationTargetItem: TypeAlias = _NotificationTargetItem_snsTopicArn


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetItem) -> dict:
    if "snsTopicArn" in value:
        return {"snsTopicArn": value["snsTopicArn"]}
    else:
        raise SerializationError("NotificationTargetItem: no variant present")


def deserialize_json(data: dict) -> NotificationTargetItem:
    if "snsTopicArn" in data:
        return {"snsTopicArn": data["snsTopicArn"]}
    else:
        raise DeserializationError("NotificationTargetItem: no recognized variant key")
