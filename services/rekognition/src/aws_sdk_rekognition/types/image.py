"""Generated from Smithy shape ``com.amazonaws.rekognition#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.image_blob
    import aws_sdk_rekognition.types.s3_object


class Image(TypedDict, closed=True):
    bytes: NotRequired["aws_sdk_rekognition.types.image_blob.ImageBlob"]
    """<p>Blob of image bytes up to 5 MBs. Note that the maximum image size you can pass to <code>DetectCustomLabels</code> is 4MB. </p>"""
    s3_object: NotRequired["aws_sdk_rekognition.types.s3_object.S3Object"]
    """<p>Identifies an S3 object as the image source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Image) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_rekognition.types.image_blob

        out["Bytes"] = aws_sdk_rekognition.types.image_blob.serialize_aws_json_1_1(
            value["bytes"]
        )
    if "s3_object" in value:
        import aws_sdk_rekognition.types.s3_object

        out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "Bytes" in data:
        import aws_sdk_rekognition.types.image_blob

        out["bytes"] = aws_sdk_rekognition.types.image_blob.deserialize_aws_json_1_1(
            data["Bytes"]
        )
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out
