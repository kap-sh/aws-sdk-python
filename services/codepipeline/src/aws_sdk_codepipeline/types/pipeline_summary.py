"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.execution_mode
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.pipeline_type
    import aws_sdk_codepipeline.types.pipeline_version
    import aws_sdk_codepipeline.types.timestamp


class PipelineSummary(TypedDict):
    name: NotRequired["aws_sdk_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    version: NotRequired["aws_sdk_codepipeline.types.pipeline_version.PipelineVersion"]
    """<p>The version number of the pipeline.</p>"""
    pipeline_type: NotRequired["aws_sdk_codepipeline.types.pipeline_type.PipelineType"]
    """<p>CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.</p> <ul> <li> <p>V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.</p> </li> <li> <p>V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.</p> </li> </ul> <important> <p>Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.</p> </important> <p>For information about pricing for CodePipeline, see <a href=\"http://aws.amazon.com/codepipeline/pricing/\">Pricing</a>.</p> <p> For information about which type of pipeline to choose, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html\">What type of pipeline is right for me?</a>.</p>"""
    execution_mode: NotRequired[
        "aws_sdk_codepipeline.types.execution_mode.ExecutionMode"
    ]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    created: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was created, in timestamp format.</p>"""
    updated: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time of the last update to the pipeline, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "pipeline_type" in value:
        import aws_sdk_codepipeline.types.pipeline_type

        out["pipelineType"] = (
            aws_sdk_codepipeline.types.pipeline_type.serialize_aws_json_1_1(
                value["pipeline_type"]
            )
        )
    if "execution_mode" in value:
        import aws_sdk_codepipeline.types.execution_mode

        out["executionMode"] = (
            aws_sdk_codepipeline.types.execution_mode.serialize_aws_json_1_1(
                value["execution_mode"]
            )
        )
    if "created" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["created"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "updated" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["updated"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["updated"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineSummary:
    out: PipelineSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "pipelineType" in data:
        import aws_sdk_codepipeline.types.pipeline_type

        out["pipeline_type"] = (
            aws_sdk_codepipeline.types.pipeline_type.deserialize_aws_json_1_1(
                data["pipelineType"]
            )
        )
    if "executionMode" in data:
        import aws_sdk_codepipeline.types.execution_mode

        out["execution_mode"] = (
            aws_sdk_codepipeline.types.execution_mode.deserialize_aws_json_1_1(
                data["executionMode"]
            )
        )
    if "created" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["created"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if "updated" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["updated"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["updated"]
        )
    return out
