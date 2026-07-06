"""Generated from Smithy shape ``com.amazonaws.comprehend#ClassifyDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_metadata
    import aws_sdk_comprehend.types.list_of_classes
    import aws_sdk_comprehend.types.list_of_document_type
    import aws_sdk_comprehend.types.list_of_errors
    import aws_sdk_comprehend.types.list_of_labels
    import aws_sdk_comprehend.types.list_of_warnings


class ClassifyDocumentResponse(TypedDict, closed=True):
    classes: NotRequired["aws_sdk_comprehend.types.list_of_classes.ListOfClasses"]
    """<p>The classes used by the document being analyzed. These are used for models trained in multi-class mode. Individual classes are mutually exclusive and each document is expected to have only a single class assigned to it. For example, an animal can be a dog or a cat, but not both at the same time. </p> <p>For prompt safety classification, the response includes only two classes (SAFE_PROMPT and UNSAFE_PROMPT), along with a confidence score for each class. The value range of the score is zero to one, where one is the highest confidence.</p>"""
    labels: NotRequired["aws_sdk_comprehend.types.list_of_labels.ListOfLabels"]
    """<p>The labels used in the document being analyzed. These are used for multi-label trained models. Individual labels represent different categories that are related in some manner and are not mutually exclusive. For example, a movie can be just an action movie, or it can be an action movie, a science fiction movie, and a comedy, all at the same time. </p>"""
    document_metadata: NotRequired[
        "aws_sdk_comprehend.types.document_metadata.DocumentMetadata"
    ]
    """<p>Extraction information about the document. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""
    document_type: NotRequired[
        "aws_sdk_comprehend.types.list_of_document_type.ListOfDocumentType"
    ]
    """<p>The document type for each page in the input document. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""
    errors: NotRequired["aws_sdk_comprehend.types.list_of_errors.ListOfErrors"]
    """<p>Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.</p>"""
    warnings: NotRequired["aws_sdk_comprehend.types.list_of_warnings.ListOfWarnings"]
    """<p>Warnings detected while processing the input document. The response includes a warning if there is a mismatch between the input document type and the model type associated with the endpoint that you specified. The response can also include warnings for individual pages that have a mismatch. </p> <p>The field is empty if the system generated no warnings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifyDocumentResponse) -> dict:
    out: dict = {}
    if "classes" in value:
        import aws_sdk_comprehend.types.list_of_classes

        out["Classes"] = (
            aws_sdk_comprehend.types.list_of_classes.serialize_aws_json_1_1(
                value["classes"]
            )
        )
    if "labels" in value:
        import aws_sdk_comprehend.types.list_of_labels

        out["Labels"] = aws_sdk_comprehend.types.list_of_labels.serialize_aws_json_1_1(
            value["labels"]
        )
    if "document_metadata" in value:
        import aws_sdk_comprehend.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_comprehend.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "document_type" in value:
        import aws_sdk_comprehend.types.list_of_document_type

        out["DocumentType"] = (
            aws_sdk_comprehend.types.list_of_document_type.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    if "errors" in value:
        import aws_sdk_comprehend.types.list_of_errors

        out["Errors"] = aws_sdk_comprehend.types.list_of_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    if "warnings" in value:
        import aws_sdk_comprehend.types.list_of_warnings

        out["Warnings"] = (
            aws_sdk_comprehend.types.list_of_warnings.serialize_aws_json_1_1(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClassifyDocumentResponse:
    out: ClassifyDocumentResponse = {}  # type: ignore[typeddict-item]
    if "Classes" in data:
        import aws_sdk_comprehend.types.list_of_classes

        out["classes"] = (
            aws_sdk_comprehend.types.list_of_classes.deserialize_aws_json_1_1(
                data["Classes"]
            )
        )
    if "Labels" in data:
        import aws_sdk_comprehend.types.list_of_labels

        out["labels"] = (
            aws_sdk_comprehend.types.list_of_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if "DocumentMetadata" in data:
        import aws_sdk_comprehend.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_comprehend.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "DocumentType" in data:
        import aws_sdk_comprehend.types.list_of_document_type

        out["document_type"] = (
            aws_sdk_comprehend.types.list_of_document_type.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    if "Errors" in data:
        import aws_sdk_comprehend.types.list_of_errors

        out["errors"] = (
            aws_sdk_comprehend.types.list_of_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    if "Warnings" in data:
        import aws_sdk_comprehend.types.list_of_warnings

        out["warnings"] = (
            aws_sdk_comprehend.types.list_of_warnings.deserialize_aws_json_1_1(
                data["Warnings"]
            )
        )
    return out
