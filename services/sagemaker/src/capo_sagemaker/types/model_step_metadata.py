"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string256


class ModelStepMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The Amazon Resource Name (ARN) of the created model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelStepMetadata:
    out: ModelStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
