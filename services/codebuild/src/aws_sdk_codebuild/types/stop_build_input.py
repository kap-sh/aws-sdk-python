"""Generated from Smithy shape ``com.amazonaws.codebuild#StopBuildInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class StopBuildInput(TypedDict):
    id: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The ID of the build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopBuildInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopBuildInput:
    out: StopBuildInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StopBuildInput.id required")
    return out
