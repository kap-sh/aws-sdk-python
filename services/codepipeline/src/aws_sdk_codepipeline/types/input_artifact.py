"""Generated from Smithy shape ``com.amazonaws.codepipeline#InputArtifact``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_name


class InputArtifact(TypedDict):
    name: "aws_sdk_codepipeline.types.artifact_name.ArtifactName"
    """<p>The name of the artifact to be worked on (for example, \"My App\").</p> <p>Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip</p> <p>The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputArtifact) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputArtifact:
    out: InputArtifact = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("InputArtifact.name required")
    return out
