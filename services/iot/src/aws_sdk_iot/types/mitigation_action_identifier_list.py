"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_identifier

MitigationActionIdentifierList: TypeAlias = list[
    "aws_sdk_iot.types.mitigation_action_identifier.MitigationActionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionIdentifierList) -> list:
    import aws_sdk_iot.types.mitigation_action_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.mitigation_action_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> MitigationActionIdentifierList:
    import aws_sdk_iot.types.mitigation_action_identifier

    out: MitigationActionIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.mitigation_action_identifier.deserialize_json(item)
        )
    return out
