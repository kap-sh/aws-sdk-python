"""Generated from Smithy shape ``com.amazonaws.kendra#InlineCustomDocumentEnrichmentConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration

InlineCustomDocumentEnrichmentConfigurationList: TypeAlias = list[
    "aws_sdk_kendra.types.inline_custom_document_enrichment_configuration.InlineCustomDocumentEnrichmentConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InlineCustomDocumentEnrichmentConfigurationList,
) -> list:
    import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.inline_custom_document_enrichment_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> InlineCustomDocumentEnrichmentConfigurationList:
    import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration

    out: InlineCustomDocumentEnrichmentConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.inline_custom_document_enrichment_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
