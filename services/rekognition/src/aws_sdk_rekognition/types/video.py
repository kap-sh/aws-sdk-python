"""Generated from Smithy shape ``com.amazonaws.rekognition#Video``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.s3_object


class Video(TypedDict):
    s3_object: NotRequired["aws_sdk_rekognition.types.s3_object.S3Object"]
    """<p>The Amazon S3 bucket name and file name for the video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Video) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import aws_sdk_rekognition.types.s3_object

        out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Video:
    out: Video = {}  # type: ignore[typeddict-item]
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out
