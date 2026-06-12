"""Generated from Smithy shape ``com.amazonaws.mq#__listOfActionRequired``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.action_required

__listOfActionRequired: TypeAlias = list[
    "aws_sdk_mq.types.action_required.ActionRequired"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfActionRequired) -> list:
    import aws_sdk_mq.types.action_required

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.action_required.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfActionRequired:
    import aws_sdk_mq.types.action_required

    out: __listOfActionRequired = []
    for item in data:
        out.append(aws_sdk_mq.types.action_required.deserialize_json(item))
    return out
