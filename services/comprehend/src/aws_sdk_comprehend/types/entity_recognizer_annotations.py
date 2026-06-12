"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerAnnotations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.s3_uri


class EntityRecognizerAnnotations(TypedDict):
    s3_uri: "aws_sdk_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""
    test_s3_uri: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p> Specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerAnnotations) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerAnnotations:
    out: EntityRecognizerAnnotations = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("EntityRecognizerAnnotations.s3_uri required")
    if "TestS3Uri" in data:
        out["test_s3_uri"] = data["TestS3Uri"]
    return out
