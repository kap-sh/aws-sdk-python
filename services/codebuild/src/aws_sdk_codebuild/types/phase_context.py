"""Generated from Smithy shape ``com.amazonaws.codebuild#PhaseContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string


class PhaseContext(TypedDict, closed=True):
    status_code: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The status code for the context of the build phase.</p>"""
    message: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>An explanation of the build phase's context. This might include a command ID and an exit code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhaseContext) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PhaseContext:
    out: PhaseContext = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out
