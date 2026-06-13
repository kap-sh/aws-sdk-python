"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDatasetLocation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.s3_uri


class _EvaluationDatasetLocation_s3Uri(TypedDict):
    s3Uri: "aws_sdk_bedrock.types.s3_uri.S3Uri"


EvaluationDatasetLocation: TypeAlias = _EvaluationDatasetLocation_s3Uri


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDatasetLocation) -> dict:
    if "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("EvaluationDatasetLocation: no variant present")


def deserialize_json(data: dict) -> EvaluationDatasetLocation:
    if "s3Uri" in data:
        return {"s3Uri": data["s3Uri"]}
    else:
        raise DeserializationError(
            "EvaluationDatasetLocation: no recognized variant key"
        )
