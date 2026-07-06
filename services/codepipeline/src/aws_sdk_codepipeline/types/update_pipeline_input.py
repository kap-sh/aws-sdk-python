"""Generated from Smithy shape ``com.amazonaws.codepipeline#UpdatePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_declaration


class UpdatePipelineInput(TypedDict, closed=True):
    pipeline: "aws_sdk_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    """<p>The name of the pipeline to be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.pipeline_declaration

    out["pipeline"] = (
        aws_sdk_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
            value["pipeline"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineInput:
    out: UpdatePipelineInput = {}  # type: ignore[typeddict-item]
    if "pipeline" in data:
        import aws_sdk_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            aws_sdk_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    else:
        raise DeserializationError("UpdatePipelineInput.pipeline required")
    return out
