"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_configuration

ActionConfigurationList: TypeAlias = list["aws_sdk_qbusiness.types.action_configuration.ActionConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConfigurationList) -> list:
    import aws_sdk_qbusiness.types.action_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.action_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionConfigurationList:
    import aws_sdk_qbusiness.types.action_configuration
    out: ActionConfigurationList = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.action_configuration.deserialize_json(item))
    return out