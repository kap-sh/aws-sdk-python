"""Generated from Smithy shape ``com.amazonaws.glue#LabelingSetGenerationTaskRunProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.uri_string


class LabelingSetGenerationTaskRunProperties(TypedDict, closed=True):
    output_s3_path: NotRequired["aws_sdk_glue.types.uri_string.UriString"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path where you will generate the labeling set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingSetGenerationTaskRunProperties) -> dict:
    out: dict = {}
    if "output_s3_path" in value:
        out["OutputS3Path"] = value["output_s3_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingSetGenerationTaskRunProperties:
    out: LabelingSetGenerationTaskRunProperties = {}  # type: ignore[typeddict-item]
    if "OutputS3Path" in data:
        out["output_s3_path"] = data["OutputS3Path"]
    return out
