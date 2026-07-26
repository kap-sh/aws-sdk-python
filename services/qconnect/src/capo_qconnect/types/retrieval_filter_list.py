"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.retrieval_filter_configuration

RetrievalFilterList: TypeAlias = list[
    "capo_qconnect.types.retrieval_filter_configuration.RetrievalFilterConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterList) -> list:
    import capo_qconnect.types.retrieval_filter_configuration

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.retrieval_filter_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievalFilterList:
    import capo_qconnect.types.retrieval_filter_configuration

    out: RetrievalFilterList = []
    for item in data:
        out.append(
            capo_qconnect.types.retrieval_filter_configuration.deserialize_json(item)
        )
    return out
