"""Generated from Smithy shape ``com.amazonaws.codebuild#StopSandboxInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class StopSandboxInput(TypedDict, closed=True):
    id: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>Information about the requested sandbox ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSandboxInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSandboxInput:
    out: StopSandboxInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StopSandboxInput.id required")
    return out
