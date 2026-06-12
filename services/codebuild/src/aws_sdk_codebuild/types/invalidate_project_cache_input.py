"""Generated from Smithy shape ``com.amazonaws.codebuild#InvalidateProjectCacheInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class InvalidateProjectCacheInput(TypedDict):
    project_name: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name of the CodeBuild build project that the cache is reset for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidateProjectCacheInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidateProjectCacheInput:
    out: InvalidateProjectCacheInput = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("InvalidateProjectCacheInput.project_name required")
    return out
