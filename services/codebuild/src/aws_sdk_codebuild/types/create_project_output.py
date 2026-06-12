"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateProjectOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project


class CreateProjectOutput(TypedDict):
    project: NotRequired["aws_sdk_codebuild.types.project.Project"]
    """<p>Information about the build project that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectOutput) -> dict:
    out: dict = {}
    if "project" in value:
        import aws_sdk_codebuild.types.project

        out["project"] = aws_sdk_codebuild.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectOutput:
    out: CreateProjectOutput = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import aws_sdk_codebuild.types.project

        out["project"] = aws_sdk_codebuild.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out
