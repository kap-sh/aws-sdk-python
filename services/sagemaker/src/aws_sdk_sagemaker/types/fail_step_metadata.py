"""Generated from Smithy shape ``com.amazonaws.sagemaker#FailStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string3072


class FailStepMetadata(TypedDict, closed=True):
    error_message: NotRequired["aws_sdk_sagemaker.types.string3072.String3072"]
    """<p>A message that you define and then is processed and rendered by the Fail step when the error occurs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailStepMetadata) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailStepMetadata:
    out: FailStepMetadata = {}  # type: ignore[typeddict-item]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
