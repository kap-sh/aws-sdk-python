"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class DeleteProjectInput(TypedDict, closed=True):
    name: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name of the build project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectInput:
    out: DeleteProjectInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteProjectInput.name required")
    return out
