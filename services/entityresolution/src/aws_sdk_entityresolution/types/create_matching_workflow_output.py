"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateMatchingWorkflowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.incremental_run_config
    import aws_sdk_entityresolution.types.input_source_config
    import aws_sdk_entityresolution.types.matching_workflow_arn
    import aws_sdk_entityresolution.types.output_source_config
    import aws_sdk_entityresolution.types.resolution_techniques


class CreateMatchingWorkflowOutput(TypedDict, closed=True):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    workflow_arn: (
        "aws_sdk_entityresolution.types.matching_workflow_arn.MatchingWorkflowArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>MatchingWorkflow</code>.</p>"""
    description: NotRequired["aws_sdk_entityresolution.types.description.Description"]
    """<p>A description of the workflow.</p>"""
    input_source_config: (
        "aws_sdk_entityresolution.types.input_source_config.InputSourceConfig"
    )
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    output_source_config: (
        "aws_sdk_entityresolution.types.output_source_config.OutputSourceConfig"
    )
    """<p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code>, <code>applyNormalization</code>, <code>KMSArn</code>, and <code>output</code>.</p>"""
    resolution_techniques: (
        "aws_sdk_entityresolution.types.resolution_techniques.ResolutionTechniques"
    )
    """<p>An object which defines the <code>resolutionType</code> and the <code>ruleBasedProperties</code>.</p>"""
    incremental_run_config: NotRequired[
        "aws_sdk_entityresolution.types.incremental_run_config.IncrementalRunConfig"
    ]
    """<p>An object which defines an incremental run type and has only <code>incrementalRunType</code> as a field.</p>"""
    role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMatchingWorkflowOutput) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
    out["workflowArn"] = value["workflow_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_entityresolution.types.input_source_config

    out["inputSourceConfig"] = (
        aws_sdk_entityresolution.types.input_source_config.serialize_json(
            value["input_source_config"]
        )
    )
    import aws_sdk_entityresolution.types.output_source_config

    out["outputSourceConfig"] = (
        aws_sdk_entityresolution.types.output_source_config.serialize_json(
            value["output_source_config"]
        )
    )
    import aws_sdk_entityresolution.types.resolution_techniques

    out["resolutionTechniques"] = (
        aws_sdk_entityresolution.types.resolution_techniques.serialize_json(
            value["resolution_techniques"]
        )
    )
    if "incremental_run_config" in value:
        import aws_sdk_entityresolution.types.incremental_run_config

        out["incrementalRunConfig"] = (
            aws_sdk_entityresolution.types.incremental_run_config.serialize_json(
                value["incremental_run_config"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CreateMatchingWorkflowOutput:
    out: CreateMatchingWorkflowOutput = {}  # type: ignore[typeddict-item]
    if "workflowName" in data:
        out["workflow_name"] = data["workflowName"]
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowOutput.workflow_name required"
        )
    if "workflowArn" in data:
        out["workflow_arn"] = data["workflowArn"]
    else:
        raise DeserializationError("CreateMatchingWorkflowOutput.workflow_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "inputSourceConfig" in data:
        import aws_sdk_entityresolution.types.input_source_config

        out["input_source_config"] = (
            aws_sdk_entityresolution.types.input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowOutput.input_source_config required"
        )
    if "outputSourceConfig" in data:
        import aws_sdk_entityresolution.types.output_source_config

        out["output_source_config"] = (
            aws_sdk_entityresolution.types.output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowOutput.output_source_config required"
        )
    if "resolutionTechniques" in data:
        import aws_sdk_entityresolution.types.resolution_techniques

        out["resolution_techniques"] = (
            aws_sdk_entityresolution.types.resolution_techniques.deserialize_json(
                data["resolutionTechniques"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowOutput.resolution_techniques required"
        )
    if "incrementalRunConfig" in data:
        import aws_sdk_entityresolution.types.incremental_run_config

        out["incremental_run_config"] = (
            aws_sdk_entityresolution.types.incremental_run_config.deserialize_json(
                data["incrementalRunConfig"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateMatchingWorkflowOutput.role_arn required")
    return out
