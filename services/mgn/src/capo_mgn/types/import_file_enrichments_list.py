"""Generated from Smithy shape ``com.amazonaws.mgn#ImportFileEnrichmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.import_file_enrichment

ImportFileEnrichmentsList: TypeAlias = list[
    "capo_mgn.types.import_file_enrichment.ImportFileEnrichment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFileEnrichmentsList) -> list:
    import capo_mgn.types.import_file_enrichment

    out: list = []
    for item in value:
        out.append(capo_mgn.types.import_file_enrichment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportFileEnrichmentsList:
    import capo_mgn.types.import_file_enrichment

    out: ImportFileEnrichmentsList = []
    for item in data:
        out.append(capo_mgn.types.import_file_enrichment.deserialize_json(item))
    return out
