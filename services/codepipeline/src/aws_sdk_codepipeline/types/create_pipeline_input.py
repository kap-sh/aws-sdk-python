"""Generated from Smithy shape ``com.amazonaws.codepipeline#CreatePipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_declaration
    import aws_sdk_codepipeline.types.tag_list


class CreatePipelineInput(TypedDict):
    pipeline: "aws_sdk_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    """<p>Represents the structure of actions and stages to be performed in the pipeline. </p>"""
    tags: NotRequired["aws_sdk_codepipeline.types.tag_list.TagList"]
    """<p>The tags for the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.pipeline_declaration

    out["pipeline"] = (
        aws_sdk_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
            value["pipeline"]
        )
    )
    if "tags" in value:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineInput:
    out: CreatePipelineInput = {}  # type: ignore[typeddict-item]
    if "pipeline" in data:
        import aws_sdk_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            aws_sdk_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    else:
        raise DeserializationError("CreatePipelineInput.pipeline required")
    if "tags" in data:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
