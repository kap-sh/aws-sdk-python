"""Generated from Smithy shape ``com.amazonaws.qbusiness#FailedDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.failed_document

FailedDocuments: TypeAlias = list["capo_qbusiness.types.failed_document.FailedDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: FailedDocuments) -> list:
    import capo_qbusiness.types.failed_document

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.failed_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedDocuments:
    import capo_qbusiness.types.failed_document

    out: FailedDocuments = []
    for item in data:
        out.append(capo_qbusiness.types.failed_document.deserialize_json(item))
    return out
