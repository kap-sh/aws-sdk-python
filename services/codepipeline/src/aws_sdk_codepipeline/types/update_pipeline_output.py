"""Generated from Smithy shape ``com.amazonaws.codepipeline#UpdatePipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_declaration


class UpdatePipelineOutput(TypedDict):
    pipeline: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    ]
    """<p>The structure of the updated pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import aws_sdk_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            aws_sdk_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
                value["pipeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineOutput:
    out: UpdatePipelineOutput = {}  # type: ignore[typeddict-item]
    if "pipeline" in data:
        import aws_sdk_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            aws_sdk_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    return out
