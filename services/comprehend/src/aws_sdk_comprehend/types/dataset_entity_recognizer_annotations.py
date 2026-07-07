"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetEntityRecognizerAnnotations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.s3_uri


class DatasetEntityRecognizerAnnotations(TypedDict, closed=True):
    s3_uri: "aws_sdk_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntityRecognizerAnnotations) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetEntityRecognizerAnnotations:
    out: DatasetEntityRecognizerAnnotations = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("DatasetEntityRecognizerAnnotations.s3_uri required")
    return out
