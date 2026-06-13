"""Generated from Smithy shape ``com.amazonaws.qbusiness#InlineDocumentEnrichmentConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.inline_document_enrichment_configuration

InlineDocumentEnrichmentConfigurations: TypeAlias = list[
    "aws_sdk_qbusiness.types.inline_document_enrichment_configuration.InlineDocumentEnrichmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineDocumentEnrichmentConfigurations) -> list:
    import aws_sdk_qbusiness.types.inline_document_enrichment_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qbusiness.types.inline_document_enrichment_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InlineDocumentEnrichmentConfigurations:
    import aws_sdk_qbusiness.types.inline_document_enrichment_configuration

    out: InlineDocumentEnrichmentConfigurations = []
    for item in data:
        out.append(
            aws_sdk_qbusiness.types.inline_document_enrichment_configuration.deserialize_json(
                item
            )
        )
    return out
