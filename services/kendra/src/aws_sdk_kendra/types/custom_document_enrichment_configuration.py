"""Generated from Smithy shape ``com.amazonaws.kendra#CustomDocumentEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.hook_configuration
    import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list
    import aws_sdk_kendra.types.role_arn


class CustomDocumentEnrichmentConfiguration(TypedDict, closed=True):
    inline_configurations: NotRequired[
        "aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list.InlineCustomDocumentEnrichmentConfigurationList"
    ]
    """<p>Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.</p>"""
    pre_extraction_hook_configuration: NotRequired[
        "aws_sdk_kendra.types.hook_configuration.HookConfiguration"
    ]
    r"""<p>Configuration information for invoking a Lambda function in Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation\">Advanced data manipulation</a>.</p>"""
    post_extraction_hook_configuration: NotRequired[
        "aws_sdk_kendra.types.hook_configuration.HookConfiguration"
    ]
    r"""<p>Configuration information for invoking a Lambda function in Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation\">Advanced data manipulation</a>.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role with permission to run <code>PreExtractionHookConfiguration</code> and <code>PostExtractionHookConfiguration</code> for altering document metadata and content during the document ingestion process. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">an IAM roles for Amazon Kendra</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDocumentEnrichmentConfiguration) -> dict:
    out: dict = {}
    if "inline_configurations" in value:
        import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list

        out["InlineConfigurations"] = (
            aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list.serialize_aws_json_1_1(
                value["inline_configurations"]
            )
        )
    if "pre_extraction_hook_configuration" in value:
        import aws_sdk_kendra.types.hook_configuration

        out["PreExtractionHookConfiguration"] = (
            aws_sdk_kendra.types.hook_configuration.serialize_aws_json_1_1(
                value["pre_extraction_hook_configuration"]
            )
        )
    if "post_extraction_hook_configuration" in value:
        import aws_sdk_kendra.types.hook_configuration

        out["PostExtractionHookConfiguration"] = (
            aws_sdk_kendra.types.hook_configuration.serialize_aws_json_1_1(
                value["post_extraction_hook_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomDocumentEnrichmentConfiguration:
    out: CustomDocumentEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "InlineConfigurations" in data:
        import aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list

        out["inline_configurations"] = (
            aws_sdk_kendra.types.inline_custom_document_enrichment_configuration_list.deserialize_aws_json_1_1(
                data["InlineConfigurations"]
            )
        )
    if "PreExtractionHookConfiguration" in data:
        import aws_sdk_kendra.types.hook_configuration

        out["pre_extraction_hook_configuration"] = (
            aws_sdk_kendra.types.hook_configuration.deserialize_aws_json_1_1(
                data["PreExtractionHookConfiguration"]
            )
        )
    if "PostExtractionHookConfiguration" in data:
        import aws_sdk_kendra.types.hook_configuration

        out["post_extraction_hook_configuration"] = (
            aws_sdk_kendra.types.hook_configuration.deserialize_aws_json_1_1(
                data["PostExtractionHookConfiguration"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
