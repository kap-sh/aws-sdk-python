"""Generated from Smithy shape ``com.amazonaws.textract#Document``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.image_blob
    import aws_sdk_textract.types.s3_object


class Document(TypedDict):
    bytes: NotRequired["aws_sdk_textract.types.image_blob.ImageBlob"]
    """<p>A blob of base64-encoded document bytes. The maximum size of a document that's provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. </p>"""
    s3_object: NotRequired["aws_sdk_textract.types.s3_object.S3Object"]
    """<p>Identifies an S3 object as the document source. The maximum size of a document that's stored in an S3 bucket is 5 MB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Document) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_textract.types.image_blob

        out["Bytes"] = aws_sdk_textract.types.image_blob.serialize_aws_json_1_1(
            value["bytes"]
        )
    if "s3_object" in value:
        import aws_sdk_textract.types.s3_object

        out["S3Object"] = aws_sdk_textract.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if "Bytes" in data:
        import aws_sdk_textract.types.image_blob

        out["bytes"] = aws_sdk_textract.types.image_blob.deserialize_aws_json_1_1(
            data["Bytes"]
        )
    if "S3Object" in data:
        import aws_sdk_textract.types.s3_object

        out["s3_object"] = aws_sdk_textract.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out
