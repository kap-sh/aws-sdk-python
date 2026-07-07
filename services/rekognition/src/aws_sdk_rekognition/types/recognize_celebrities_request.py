"""Generated from Smithy shape ``com.amazonaws.rekognition#RecognizeCelebritiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.image


class RecognizeCelebritiesRequest(TypedDict, closed=True):
    image: "aws_sdk_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecognizeCelebritiesRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecognizeCelebritiesRequest:
    out: RecognizeCelebritiesRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("RecognizeCelebritiesRequest.image required")
    return out
