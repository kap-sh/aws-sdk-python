"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string1024


class JobStepMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.string1024.String1024"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker job that was run by this step execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobStepMetadata:
    out: JobStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
