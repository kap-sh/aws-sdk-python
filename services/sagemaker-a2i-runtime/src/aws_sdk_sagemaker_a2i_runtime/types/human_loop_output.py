"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.string


class HumanLoopOutput(TypedDict):
    output_s3_uri: NotRequired["aws_sdk_sagemaker_a2i_runtime.types.string.String"]
    """<p>The location of the Amazon S3 object where Amazon Augmented AI stores your human loop output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopOutput) -> dict:
    out: dict = {}
    if "output_s3_uri" in value:
        out["OutputS3Uri"] = value["output_s3_uri"]
    return out


def deserialize_json(data: dict) -> HumanLoopOutput:
    out: HumanLoopOutput = {}  # type: ignore[typeddict-item]
    if "OutputS3Uri" in data:
        out["output_s3_uri"] = data["OutputS3Uri"]
    return out
