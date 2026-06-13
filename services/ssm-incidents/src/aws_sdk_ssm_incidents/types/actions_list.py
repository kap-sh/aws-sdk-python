"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.action

ActionsList: TypeAlias = list["aws_sdk_ssm_incidents.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionsList) -> list:
    import aws_sdk_ssm_incidents.types.action

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_incidents.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionsList:
    import aws_sdk_ssm_incidents.types.action

    out: ActionsList = []
    for item in data:
        out.append(aws_sdk_ssm_incidents.types.action.deserialize_json(item))
    return out
