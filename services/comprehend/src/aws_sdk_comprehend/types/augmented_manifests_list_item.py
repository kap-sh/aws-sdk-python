"""Generated from Smithy shape ``com.amazonaws.comprehend#AugmentedManifestsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.attribute_names_list
    import aws_sdk_comprehend.types.augmented_manifests_document_type_format
    import aws_sdk_comprehend.types.s3_uri
    import aws_sdk_comprehend.types.split


class AugmentedManifestsListItem(TypedDict, closed=True):
    s3_uri: "aws_sdk_comprehend.types.s3_uri.S3Uri"
    """<p>The Amazon S3 location of the augmented manifest file.</p>"""
    split: NotRequired["aws_sdk_comprehend.types.split.Split"]
    """<p>The purpose of the data you've provided in the augmented manifest. You can either train or test this data. If you don't specify, the default is train.</p> <p>TRAIN - all of the documents in the manifest will be used for training. If no test documents are provided, Amazon Comprehend will automatically reserve a portion of the training documents for testing.</p> <p> TEST - all of the documents in the manifest will be used for testing.</p>"""
    attribute_names: "aws_sdk_comprehend.types.attribute_names_list.AttributeNamesList"
    """<p>The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.</p> <p>If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.</p> <p>If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.</p>"""
    annotation_data_s3_uri: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 prefix to the annotation files that are referred in the augmented manifest file.</p>"""
    source_documents_s3_uri: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.</p>"""
    document_type: NotRequired[
        "aws_sdk_comprehend.types.augmented_manifests_document_type_format.AugmentedManifestsDocumentTypeFormat"
    ]
    """<p>The type of augmented manifest. PlainTextDocument or SemiStructuredDocument. If you don't specify, the default is PlainTextDocument. </p> <ul> <li> <p> <code>PLAIN_TEXT_DOCUMENT</code> A document type that represents any unicode text that is encoded in UTF-8.</p> </li> <li> <p> <code>SEMI_STRUCTURED_DOCUMENT</code> A document type with positional and structural context, like a PDF. For training with Amazon Comprehend, only PDFs are supported. For inference, Amazon Comprehend support PDFs, DOCX and TXT.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AugmentedManifestsListItem) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "split" in value:
        import aws_sdk_comprehend.types.split

        out["Split"] = aws_sdk_comprehend.types.split.serialize_aws_json_1_1(
            value["split"]
        )
    import aws_sdk_comprehend.types.attribute_names_list

    out["AttributeNames"] = (
        aws_sdk_comprehend.types.attribute_names_list.serialize_aws_json_1_1(
            value["attribute_names"]
        )
    )
    if "annotation_data_s3_uri" in value:
        out["AnnotationDataS3Uri"] = value["annotation_data_s3_uri"]
    if "source_documents_s3_uri" in value:
        out["SourceDocumentsS3Uri"] = value["source_documents_s3_uri"]
    if "document_type" in value:
        import aws_sdk_comprehend.types.augmented_manifests_document_type_format

        out["DocumentType"] = (
            aws_sdk_comprehend.types.augmented_manifests_document_type_format.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AugmentedManifestsListItem:
    out: AugmentedManifestsListItem = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("AugmentedManifestsListItem.s3_uri required")
    if "Split" in data:
        import aws_sdk_comprehend.types.split

        out["split"] = aws_sdk_comprehend.types.split.deserialize_aws_json_1_1(
            data["Split"]
        )
    if "AttributeNames" in data:
        import aws_sdk_comprehend.types.attribute_names_list

        out["attribute_names"] = (
            aws_sdk_comprehend.types.attribute_names_list.deserialize_aws_json_1_1(
                data["AttributeNames"]
            )
        )
    else:
        raise DeserializationError(
            "AugmentedManifestsListItem.attribute_names required"
        )
    if "AnnotationDataS3Uri" in data:
        out["annotation_data_s3_uri"] = data["AnnotationDataS3Uri"]
    if "SourceDocumentsS3Uri" in data:
        out["source_documents_s3_uri"] = data["SourceDocumentsS3Uri"]
    if "DocumentType" in data:
        import aws_sdk_comprehend.types.augmented_manifests_document_type_format

        out["document_type"] = (
            aws_sdk_comprehend.types.augmented_manifests_document_type_format.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    return out
