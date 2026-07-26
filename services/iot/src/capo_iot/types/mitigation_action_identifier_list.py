"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_identifier

MitigationActionIdentifierList: TypeAlias = list[
    "capo_iot.types.mitigation_action_identifier.MitigationActionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionIdentifierList) -> list:
    import capo_iot.types.mitigation_action_identifier

    out: list = []
    for item in value:
        out.append(capo_iot.types.mitigation_action_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> MitigationActionIdentifierList:
    import capo_iot.types.mitigation_action_identifier

    out: MitigationActionIdentifierList = []
    for item in data:
        out.append(capo_iot.types.mitigation_action_identifier.deserialize_json(item))
    return out
