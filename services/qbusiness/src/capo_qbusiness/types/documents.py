"""Generated from Smithy shape ``com.amazonaws.qbusiness#Documents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document

Documents: TypeAlias = list["capo_qbusiness.types.document.Document"]


# --- restJson1 ser/de ---
def serialize_json(value: Documents) -> list:
    import capo_qbusiness.types.document

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document.serialize_json(item))
    return out


def deserialize_json(data: list) -> Documents:
    import capo_qbusiness.types.document

    out: Documents = []
    for item in data:
        out.append(capo_qbusiness.types.document.deserialize_json(item))
    return out
