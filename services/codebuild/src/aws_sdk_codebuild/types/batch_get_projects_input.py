"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetProjectsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_names


class BatchGetProjectsInput(TypedDict):
    names: "aws_sdk_codebuild.types.project_names.ProjectNames"
    """<p>The names or ARNs of the build projects. To get information about a project shared with your Amazon Web Services account, its ARN must be specified. You cannot specify a shared project using its name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetProjectsInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.project_names

    out["names"] = aws_sdk_codebuild.types.project_names.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetProjectsInput:
    out: BatchGetProjectsInput = {}  # type: ignore[typeddict-item]
    if "names" in data:
        import aws_sdk_codebuild.types.project_names

        out["names"] = aws_sdk_codebuild.types.project_names.deserialize_aws_json_1_1(
            data["names"]
        )
    else:
        raise DeserializationError("BatchGetProjectsInput.names required")
    return out
