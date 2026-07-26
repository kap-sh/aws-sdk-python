"""Generated from Smithy shape ``com.amazonaws.qbusiness#Retrievers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.retriever

Retrievers: TypeAlias = list["capo_qbusiness.types.retriever.Retriever"]


# --- restJson1 ser/de ---
def serialize_json(value: Retrievers) -> list:
    import capo_qbusiness.types.retriever

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.retriever.serialize_json(item))
    return out


def deserialize_json(data: list) -> Retrievers:
    import capo_qbusiness.types.retriever

    out: Retrievers = []
    for item in data:
        out.append(capo_qbusiness.types.retriever.deserialize_json(item))
    return out
