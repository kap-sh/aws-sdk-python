"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerDocuments``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.input_format
    import aws_sdk_comprehend.types.s3_uri


class EntityRecognizerDocuments(TypedDict):
    s3_uri: "aws_sdk_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""
    test_s3_uri: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p> Specifies the Amazon S3 location where the test documents for an entity recognizer are located. The URI must be in the same Amazon Web Services Region as the API endpoint that you are calling.</p>"""
    input_format: NotRequired["aws_sdk_comprehend.types.input_format.InputFormat"]
    """<p> Specifies how the text in an input file should be processed. This is optional, and the default is ONE_DOC_PER_LINE. ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerDocuments) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    if "input_format" in value:
        import aws_sdk_comprehend.types.input_format

        out["InputFormat"] = (
            aws_sdk_comprehend.types.input_format.serialize_aws_json_1_1(
                value["input_format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerDocuments:
    out: EntityRecognizerDocuments = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("EntityRecognizerDocuments.s3_uri required")
    if "TestS3Uri" in data:
        out["test_s3_uri"] = data["TestS3Uri"]
    if "InputFormat" in data:
        import aws_sdk_comprehend.types.input_format

        out["input_format"] = (
            aws_sdk_comprehend.types.input_format.deserialize_aws_json_1_1(
                data["InputFormat"]
            )
        )
    return out
