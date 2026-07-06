"""Generated from Smithy shape ``com.amazonaws.sagemaker#RegisterModelStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string256


class RegisterModelStepMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterModelStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterModelStepMetadata:
    out: RegisterModelStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
