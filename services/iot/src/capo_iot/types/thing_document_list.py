"""Generated from Smithy shape ``com.amazonaws.iot#ThingDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_document

ThingDocumentList: TypeAlias = list["capo_iot.types.thing_document.ThingDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: ThingDocumentList) -> list:
    import capo_iot.types.thing_document

    out: list = []
    for item in value:
        out.append(capo_iot.types.thing_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingDocumentList:
    import capo_iot.types.thing_document

    out: ThingDocumentList = []
    for item in data:
        out.append(capo_iot.types.thing_document.deserialize_json(item))
    return out
