"""Generated from Smithy shape ``com.amazonaws.comprehend#ClassifyDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.customer_input_string
    import aws_sdk_comprehend.types.document_classifier_endpoint_arn
    import aws_sdk_comprehend.types.document_reader_config
    import aws_sdk_comprehend.types.semi_structured_document_blob


class ClassifyDocumentRequest(TypedDict, closed=True):
    text: NotRequired[
        "aws_sdk_comprehend.types.customer_input_string.CustomerInputString"
    ]
    """<p>The document text to be analyzed. If you enter text using this parameter, do not use the <code>Bytes</code> parameter.</p>"""
    endpoint_arn: "aws_sdk_comprehend.types.document_classifier_endpoint_arn.DocumentClassifierEndpointArn"
    r"""<p>The Amazon Resource Number (ARN) of the endpoint. </p> <p>For prompt safety classification, Amazon Comprehend provides the endpoint ARN. For more information about prompt safety classifiers, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification\">Prompt safety classification</a> in the <i>Amazon Comprehend Developer Guide</i> </p> <p>For custom classification, you create an endpoint for your custom model. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/using-endpoints.html\">Using Amazon Comprehend endpoints</a>.</p>"""
    bytes: NotRequired[
        "aws_sdk_comprehend.types.semi_structured_document_blob.SemiStructuredDocumentBlob"
    ]
    r"""<p>Use the <code>Bytes</code> parameter to input a text, PDF, Word or image file.</p> <p>When you classify a document using a custom model, you can also use the <code>Bytes</code> parameter to input an Amazon Textract <code>DetectDocumentText</code> or <code>AnalyzeDocument</code> output file.</p> <p>To classify a document using the prompt safety classifier, use the <code>Text</code> parameter for input.</p> <p>Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to classify documents, the SDK may encode the document file bytes for you. </p> <p>The maximum length of this field depends on the input document type. For details, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html\"> Inputs for real-time custom analysis</a> in the Comprehend Developer Guide. </p> <p>If you use the <code>Bytes</code> parameter, do not use the <code>Text</code> parameter.</p>"""
    document_reader_config: NotRequired[
        "aws_sdk_comprehend.types.document_reader_config.DocumentReaderConfig"
    ]
    """<p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifyDocumentRequest) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    out["EndpointArn"] = value["endpoint_arn"]
    if "bytes" in value:
        import aws_sdk_comprehend.types.semi_structured_document_blob

        out["Bytes"] = (
            aws_sdk_comprehend.types.semi_structured_document_blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "document_reader_config" in value:
        import aws_sdk_comprehend.types.document_reader_config

        out["DocumentReaderConfig"] = (
            aws_sdk_comprehend.types.document_reader_config.serialize_aws_json_1_1(
                value["document_reader_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClassifyDocumentRequest:
    out: ClassifyDocumentRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError("ClassifyDocumentRequest.endpoint_arn required")
    if "Bytes" in data:
        import aws_sdk_comprehend.types.semi_structured_document_blob

        out["bytes"] = (
            aws_sdk_comprehend.types.semi_structured_document_blob.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if "DocumentReaderConfig" in data:
        import aws_sdk_comprehend.types.document_reader_config

        out["document_reader_config"] = (
            aws_sdk_comprehend.types.document_reader_config.deserialize_aws_json_1_1(
                data["DocumentReaderConfig"]
            )
        )
    return out
