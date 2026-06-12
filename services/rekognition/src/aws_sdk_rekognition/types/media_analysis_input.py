"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.s3_object


class MediaAnalysisInput(TypedDict):
    s3_object: "aws_sdk_rekognition.types.s3_object.S3Object"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisInput) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.s3_object

    out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
        value["s3_object"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisInput:
    out: MediaAnalysisInput = {}  # type: ignore[typeddict-item]
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    else:
        raise DeserializationError("MediaAnalysisInput.s3_object required")
    return out
