"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListPipelinesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.next_token
    import aws_sdk_codepipeline.types.pipeline_list


class ListPipelinesOutput(TypedDict):
    pipelines: NotRequired["aws_sdk_codepipeline.types.pipeline_list.PipelineList"]
    """<p>The list of pipelines.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list pipelines call to return the next set of pipelines in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesOutput) -> dict:
    out: dict = {}
    if "pipelines" in value:
        import aws_sdk_codepipeline.types.pipeline_list

        out["pipelines"] = (
            aws_sdk_codepipeline.types.pipeline_list.serialize_aws_json_1_1(
                value["pipelines"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesOutput:
    out: ListPipelinesOutput = {}  # type: ignore[typeddict-item]
    if "pipelines" in data:
        import aws_sdk_codepipeline.types.pipeline_list

        out["pipelines"] = (
            aws_sdk_codepipeline.types.pipeline_list.deserialize_aws_json_1_1(
                data["pipelines"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
