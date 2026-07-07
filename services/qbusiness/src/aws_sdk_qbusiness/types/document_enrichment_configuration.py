"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.hook_configuration
    import aws_sdk_qbusiness.types.inline_document_enrichment_configurations


class DocumentEnrichmentConfiguration(TypedDict, closed=True):
    inline_configurations: NotRequired[
        "aws_sdk_qbusiness.types.inline_document_enrichment_configurations.InlineDocumentEnrichmentConfigurations"
    ]
    """<p>Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.</p>"""
    pre_extraction_hook_configuration: NotRequired[
        "aws_sdk_qbusiness.types.hook_configuration.HookConfiguration"
    ]
    post_extraction_hook_configuration: NotRequired[
        "aws_sdk_qbusiness.types.hook_configuration.HookConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentEnrichmentConfiguration) -> dict:
    out: dict = {}
    if "inline_configurations" in value:
        import aws_sdk_qbusiness.types.inline_document_enrichment_configurations

        out["inlineConfigurations"] = (
            aws_sdk_qbusiness.types.inline_document_enrichment_configurations.serialize_json(
                value["inline_configurations"]
            )
        )
    if "pre_extraction_hook_configuration" in value:
        import aws_sdk_qbusiness.types.hook_configuration

        out["preExtractionHookConfiguration"] = (
            aws_sdk_qbusiness.types.hook_configuration.serialize_json(
                value["pre_extraction_hook_configuration"]
            )
        )
    if "post_extraction_hook_configuration" in value:
        import aws_sdk_qbusiness.types.hook_configuration

        out["postExtractionHookConfiguration"] = (
            aws_sdk_qbusiness.types.hook_configuration.serialize_json(
                value["post_extraction_hook_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentEnrichmentConfiguration:
    out: DocumentEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "inlineConfigurations" in data:
        import aws_sdk_qbusiness.types.inline_document_enrichment_configurations

        out["inline_configurations"] = (
            aws_sdk_qbusiness.types.inline_document_enrichment_configurations.deserialize_json(
                data["inlineConfigurations"]
            )
        )
    if "preExtractionHookConfiguration" in data:
        import aws_sdk_qbusiness.types.hook_configuration

        out["pre_extraction_hook_configuration"] = (
            aws_sdk_qbusiness.types.hook_configuration.deserialize_json(
                data["preExtractionHookConfiguration"]
            )
        )
    if "postExtractionHookConfiguration" in data:
        import aws_sdk_qbusiness.types.hook_configuration

        out["post_extraction_hook_configuration"] = (
            aws_sdk_qbusiness.types.hook_configuration.deserialize_json(
                data["postExtractionHookConfiguration"]
            )
        )
    return out
