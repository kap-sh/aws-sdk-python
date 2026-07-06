"""Generated from Smithy shape ``com.amazonaws.rekognition#Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.s3_object


class Summary(TypedDict, closed=True):
    s3_object: NotRequired["aws_sdk_rekognition.types.s3_object.S3Object"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Summary) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import aws_sdk_rekognition.types.s3_object

        out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out
