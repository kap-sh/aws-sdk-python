"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action

MitigationActionList: TypeAlias = list[
    "aws_sdk_iot.types.mitigation_action.MitigationAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionList) -> list:
    import aws_sdk_iot.types.mitigation_action

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.mitigation_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> MitigationActionList:
    import aws_sdk_iot.types.mitigation_action

    out: MitigationActionList = []
    for item in data:
        out.append(aws_sdk_iot.types.mitigation_action.deserialize_json(item))
    return out
