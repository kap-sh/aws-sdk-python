"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_group_document

ThingGroupDocumentList: TypeAlias = list[
    "capo_iot.types.thing_group_document.ThingGroupDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupDocumentList) -> list:
    import capo_iot.types.thing_group_document

    out: list = []
    for item in value:
        out.append(capo_iot.types.thing_group_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingGroupDocumentList:
    import capo_iot.types.thing_group_document

    out: ThingGroupDocumentList = []
    for item in data:
        out.append(capo_iot.types.thing_group_document.deserialize_json(item))
    return out
