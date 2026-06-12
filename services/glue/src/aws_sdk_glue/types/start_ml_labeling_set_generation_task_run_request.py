"""Generated from Smithy shape ``com.amazonaws.glue#StartMLLabelingSetGenerationTaskRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.uri_string


class StartMLLabelingSetGenerationTaskRunRequest(TypedDict):
    transform_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    output_s3_path: "aws_sdk_glue.types.uri_string.UriString"
    """<p>The Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMLLabelingSetGenerationTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    out["OutputS3Path"] = value["output_s3_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMLLabelingSetGenerationTaskRunRequest:
    out: StartMLLabelingSetGenerationTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError(
            "StartMLLabelingSetGenerationTaskRunRequest.transform_id required"
        )
    if "OutputS3Path" in data:
        out["output_s3_path"] = data["OutputS3Path"]
    else:
        raise DeserializationError(
            "StartMLLabelingSetGenerationTaskRunRequest.output_s3_path required"
        )
    return out
