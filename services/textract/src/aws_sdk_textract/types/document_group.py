"""Generated from Smithy shape ``com.amazonaws.textract#DocumentGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.detected_signature_list
    import aws_sdk_textract.types.non_empty_string
    import aws_sdk_textract.types.split_document_list
    import aws_sdk_textract.types.undetected_signature_list


class DocumentGroup(TypedDict, closed=True):
    type: NotRequired["aws_sdk_textract.types.non_empty_string.NonEmptyString"]
    r"""<p>The type of document that Amazon Textract has detected. See <a href=\"https://docs.aws.amazon.com/textract/latest/dg/lending-response-objects.html\">Analyze Lending Response Objects</a> for a list of all types returned by Textract.</p>"""
    split_documents: NotRequired[
        "aws_sdk_textract.types.split_document_list.SplitDocumentList"
    ]
    """<p>An array that contains information about the pages of a document, defined by logical boundary.</p>"""
    detected_signatures: NotRequired[
        "aws_sdk_textract.types.detected_signature_list.DetectedSignatureList"
    ]
    """<p>A list of the detected signatures found in a document group.</p>"""
    undetected_signatures: NotRequired[
        "aws_sdk_textract.types.undetected_signature_list.UndetectedSignatureList"
    ]
    """<p>A list of any expected signatures not found in a document group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentGroup) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "split_documents" in value:
        import aws_sdk_textract.types.split_document_list

        out["SplitDocuments"] = (
            aws_sdk_textract.types.split_document_list.serialize_aws_json_1_1(
                value["split_documents"]
            )
        )
    if "detected_signatures" in value:
        import aws_sdk_textract.types.detected_signature_list

        out["DetectedSignatures"] = (
            aws_sdk_textract.types.detected_signature_list.serialize_aws_json_1_1(
                value["detected_signatures"]
            )
        )
    if "undetected_signatures" in value:
        import aws_sdk_textract.types.undetected_signature_list

        out["UndetectedSignatures"] = (
            aws_sdk_textract.types.undetected_signature_list.serialize_aws_json_1_1(
                value["undetected_signatures"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentGroup:
    out: DocumentGroup = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "SplitDocuments" in data:
        import aws_sdk_textract.types.split_document_list

        out["split_documents"] = (
            aws_sdk_textract.types.split_document_list.deserialize_aws_json_1_1(
                data["SplitDocuments"]
            )
        )
    if "DetectedSignatures" in data:
        import aws_sdk_textract.types.detected_signature_list

        out["detected_signatures"] = (
            aws_sdk_textract.types.detected_signature_list.deserialize_aws_json_1_1(
                data["DetectedSignatures"]
            )
        )
    if "UndetectedSignatures" in data:
        import aws_sdk_textract.types.undetected_signature_list

        out["undetected_signatures"] = (
            aws_sdk_textract.types.undetected_signature_list.deserialize_aws_json_1_1(
                data["UndetectedSignatures"]
            )
        )
    return out
