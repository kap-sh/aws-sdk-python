"""Generated from Smithy shape ``com.amazonaws.codebuild#StartBuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build


class StartBuildOutput(TypedDict, closed=True):
    build: NotRequired["aws_sdk_codebuild.types.build.Build"]
    """<p>Information about the build to be run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import aws_sdk_codebuild.types.build

        out["build"] = aws_sdk_codebuild.types.build.serialize_aws_json_1_1(
            value["build"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBuildOutput:
    out: StartBuildOutput = {}  # type: ignore[typeddict-item]
    if "build" in data:
        import aws_sdk_codebuild.types.build

        out["build"] = aws_sdk_codebuild.types.build.deserialize_aws_json_1_1(
            data["build"]
        )
    return out
