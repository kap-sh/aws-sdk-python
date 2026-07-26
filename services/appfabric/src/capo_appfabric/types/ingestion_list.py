"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appfabric.types.ingestion_summary

IngestionList: TypeAlias = list[
    "capo_appfabric.types.ingestion_summary.IngestionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionList) -> list:
    import capo_appfabric.types.ingestion_summary

    out: list = []
    for item in value:
        out.append(capo_appfabric.types.ingestion_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> IngestionList:
    import capo_appfabric.types.ingestion_summary

    out: IngestionList = []
    for item in data:
        out.append(capo_appfabric.types.ingestion_summary.deserialize_json(item))
    return out
