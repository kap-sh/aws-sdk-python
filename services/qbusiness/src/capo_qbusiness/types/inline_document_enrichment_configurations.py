"""Generated from Smithy shape ``com.amazonaws.qbusiness#InlineDocumentEnrichmentConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.inline_document_enrichment_configuration

InlineDocumentEnrichmentConfigurations: TypeAlias = list[
    "capo_qbusiness.types.inline_document_enrichment_configuration.InlineDocumentEnrichmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineDocumentEnrichmentConfigurations) -> list:
    import capo_qbusiness.types.inline_document_enrichment_configuration

    out: list = []
    for item in value:
        out.append(
            capo_qbusiness.types.inline_document_enrichment_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InlineDocumentEnrichmentConfigurations:
    import capo_qbusiness.types.inline_document_enrichment_configuration

    out: InlineDocumentEnrichmentConfigurations = []
    for item in data:
        out.append(
            capo_qbusiness.types.inline_document_enrichment_configuration.deserialize_json(
                item
            )
        )
    return out
