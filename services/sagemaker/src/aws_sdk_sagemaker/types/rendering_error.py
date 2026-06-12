"""Generated from Smithy shape ``com.amazonaws.sagemaker#RenderingError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class RenderingError(TypedDict):
    code: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A unique identifier for a specific class of errors.</p>"""
    message: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A human-readable message describing the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenderingError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenderingError:
    out: RenderingError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
