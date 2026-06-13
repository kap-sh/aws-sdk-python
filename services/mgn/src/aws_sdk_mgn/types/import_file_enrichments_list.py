"""Generated from Smithy shape ``com.amazonaws.mgn#ImportFileEnrichmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_file_enrichment

ImportFileEnrichmentsList: TypeAlias = list[
    "aws_sdk_mgn.types.import_file_enrichment.ImportFileEnrichment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFileEnrichmentsList) -> list:
    import aws_sdk_mgn.types.import_file_enrichment

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.import_file_enrichment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportFileEnrichmentsList:
    import aws_sdk_mgn.types.import_file_enrichment

    out: ImportFileEnrichmentsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.import_file_enrichment.deserialize_json(item))
    return out
