"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_store
    import aws_sdk_codepipeline.types.artifact_store_map
    import aws_sdk_codepipeline.types.execution_mode
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.pipeline_stage_declaration_list
    import aws_sdk_codepipeline.types.pipeline_trigger_declaration_list
    import aws_sdk_codepipeline.types.pipeline_type
    import aws_sdk_codepipeline.types.pipeline_variable_declaration_list
    import aws_sdk_codepipeline.types.pipeline_version
    import aws_sdk_codepipeline.types.role_arn


class PipelineDeclaration(TypedDict):
    name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline.</p>"""
    role_arn: "aws_sdk_codepipeline.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no <code>actionRoleArn</code>, or to use to assume roles for actions with an <code>actionRoleArn</code>.</p>"""
    artifact_store: NotRequired[
        "aws_sdk_codepipeline.types.artifact_store.ArtifactStore"
    ]
    """<p>Represents information about the S3 bucket where artifacts are stored for the pipeline.</p> <note> <p>You must include either <code>artifactStore</code> or <code>artifactStores</code> in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use <code>artifactStores</code>.</p> </note>"""
    artifact_stores: NotRequired[
        "aws_sdk_codepipeline.types.artifact_store_map.ArtifactStoreMap"
    ]
    """<p>A mapping of <code>artifactStore</code> objects and their corresponding Amazon Web Services Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.</p> <note> <p>You must include either <code>artifactStore</code> or <code>artifactStores</code> in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use <code>artifactStores</code>.</p> </note>"""
    stages: "aws_sdk_codepipeline.types.pipeline_stage_declaration_list.PipelineStageDeclarationList"
    """<p>The stage in which to perform the action.</p>"""
    version: NotRequired["aws_sdk_codepipeline.types.pipeline_version.PipelineVersion"]
    """<p>The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.</p>"""
    execution_mode: NotRequired[
        "aws_sdk_codepipeline.types.execution_mode.ExecutionMode"
    ]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    pipeline_type: NotRequired["aws_sdk_codepipeline.types.pipeline_type.PipelineType"]
    r"""<p>CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.</p> <ul> <li> <p>V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.</p> </li> <li> <p>V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.</p> </li> </ul> <important> <p>Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.</p> </important> <p>For information about pricing for CodePipeline, see <a href=\"http://aws.amazon.com/codepipeline/pricing/\">Pricing</a>.</p> <p> For information about which type of pipeline to choose, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html\">What type of pipeline is right for me?</a>.</p>"""
    variables: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_variable_declaration_list.PipelineVariableDeclarationList"
    ]
    r"""<p>A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9@\-_]+</code>.</p>"""
    triggers: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_trigger_declaration_list.PipelineTriggerDeclarationList"
    ]
    """<p>The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.</p> <note> <p>When a trigger configuration is specified, default change detection for repository and branch commits is disabled.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["roleArn"] = value["role_arn"]
    if "artifact_store" in value:
        import aws_sdk_codepipeline.types.artifact_store

        out["artifactStore"] = (
            aws_sdk_codepipeline.types.artifact_store.serialize_aws_json_1_1(
                value["artifact_store"]
            )
        )
    if "artifact_stores" in value:
        import aws_sdk_codepipeline.types.artifact_store_map

        out["artifactStores"] = (
            aws_sdk_codepipeline.types.artifact_store_map.serialize_aws_json_1_1(
                value["artifact_stores"]
            )
        )
    import aws_sdk_codepipeline.types.pipeline_stage_declaration_list

    out["stages"] = (
        aws_sdk_codepipeline.types.pipeline_stage_declaration_list.serialize_aws_json_1_1(
            value["stages"]
        )
    )
    if "version" in value:
        out["version"] = value["version"]
    if "execution_mode" in value:
        import aws_sdk_codepipeline.types.execution_mode

        out["executionMode"] = (
            aws_sdk_codepipeline.types.execution_mode.serialize_aws_json_1_1(
                value["execution_mode"]
            )
        )
    if "pipeline_type" in value:
        import aws_sdk_codepipeline.types.pipeline_type

        out["pipelineType"] = (
            aws_sdk_codepipeline.types.pipeline_type.serialize_aws_json_1_1(
                value["pipeline_type"]
            )
        )
    if "variables" in value:
        import aws_sdk_codepipeline.types.pipeline_variable_declaration_list

        out["variables"] = (
            aws_sdk_codepipeline.types.pipeline_variable_declaration_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "triggers" in value:
        import aws_sdk_codepipeline.types.pipeline_trigger_declaration_list

        out["triggers"] = (
            aws_sdk_codepipeline.types.pipeline_trigger_declaration_list.serialize_aws_json_1_1(
                value["triggers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineDeclaration:
    out: PipelineDeclaration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineDeclaration.name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PipelineDeclaration.role_arn required")
    if "artifactStore" in data:
        import aws_sdk_codepipeline.types.artifact_store

        out["artifact_store"] = (
            aws_sdk_codepipeline.types.artifact_store.deserialize_aws_json_1_1(
                data["artifactStore"]
            )
        )
    if "artifactStores" in data:
        import aws_sdk_codepipeline.types.artifact_store_map

        out["artifact_stores"] = (
            aws_sdk_codepipeline.types.artifact_store_map.deserialize_aws_json_1_1(
                data["artifactStores"]
            )
        )
    if "stages" in data:
        import aws_sdk_codepipeline.types.pipeline_stage_declaration_list

        out["stages"] = (
            aws_sdk_codepipeline.types.pipeline_stage_declaration_list.deserialize_aws_json_1_1(
                data["stages"]
            )
        )
    else:
        raise DeserializationError("PipelineDeclaration.stages required")
    if "version" in data:
        out["version"] = data["version"]
    if "executionMode" in data:
        import aws_sdk_codepipeline.types.execution_mode

        out["execution_mode"] = (
            aws_sdk_codepipeline.types.execution_mode.deserialize_aws_json_1_1(
                data["executionMode"]
            )
        )
    if "pipelineType" in data:
        import aws_sdk_codepipeline.types.pipeline_type

        out["pipeline_type"] = (
            aws_sdk_codepipeline.types.pipeline_type.deserialize_aws_json_1_1(
                data["pipelineType"]
            )
        )
    if "variables" in data:
        import aws_sdk_codepipeline.types.pipeline_variable_declaration_list

        out["variables"] = (
            aws_sdk_codepipeline.types.pipeline_variable_declaration_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "triggers" in data:
        import aws_sdk_codepipeline.types.pipeline_trigger_declaration_list

        out["triggers"] = (
            aws_sdk_codepipeline.types.pipeline_trigger_declaration_list.deserialize_aws_json_1_1(
                data["triggers"]
            )
        )
    return out
