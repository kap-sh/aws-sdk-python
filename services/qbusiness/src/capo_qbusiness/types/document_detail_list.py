"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_details

DocumentDetailList: TypeAlias = list[
    "capo_qbusiness.types.document_details.DocumentDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentDetailList) -> list:
    import capo_qbusiness.types.document_details

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentDetailList:
    import capo_qbusiness.types.document_details

    out: DocumentDetailList = []
    for item in data:
        out.append(capo_qbusiness.types.document_details.deserialize_json(item))
    return out
