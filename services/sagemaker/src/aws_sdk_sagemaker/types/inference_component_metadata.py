"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string2048


class InferenceComponentMetadata(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.string2048.String2048"]
    """<p> The Amazon Resource Name (ARN) of the inference component. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentMetadata:
    out: InferenceComponentMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
