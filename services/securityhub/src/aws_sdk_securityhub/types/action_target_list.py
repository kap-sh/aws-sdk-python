"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.action_target

ActionTargetList: TypeAlias = list[
    "aws_sdk_securityhub.types.action_target.ActionTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionTargetList) -> list:
    import aws_sdk_securityhub.types.action_target

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.action_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionTargetList:
    import aws_sdk_securityhub.types.action_target

    out: ActionTargetList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.action_target.deserialize_json(item))
    return out
