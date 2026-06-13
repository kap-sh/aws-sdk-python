"""Generated from Smithy shape ``com.amazonaws.entityresolution#UpdateIdMappingWorkflowInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.id_mapping_incremental_run_config
    import aws_sdk_entityresolution.types.id_mapping_role_arn
    import aws_sdk_entityresolution.types.id_mapping_techniques
    import aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config
    import aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config


class UpdateIdMappingWorkflowInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    description: NotRequired["aws_sdk_entityresolution.types.description.Description"]
    """<p>A description of the workflow.</p>"""
    input_source_config: "aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config.IdMappingWorkflowInputSourceConfig"
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    output_source_config: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config.IdMappingWorkflowOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code> and <code>KMSArn</code>.</p>"""
    id_mapping_techniques: (
        "aws_sdk_entityresolution.types.id_mapping_techniques.IdMappingTechniques"
    )
    """<p>An object which defines the ID mapping technique and any additional configurations.</p>"""
    incremental_run_config: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_incremental_run_config.IdMappingIncrementalRunConfig"
    ]
    """<p> The incremental run configuration for the update ID mapping workflow.</p>"""
    role_arn: "aws_sdk_entityresolution.types.id_mapping_role_arn.IdMappingRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access Amazon Web Services resources on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdMappingWorkflowInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config

    out["inputSourceConfig"] = (
        aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config.serialize_json(
            value["input_source_config"]
        )
    )
    if "output_source_config" in value:
        import aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config

        out["outputSourceConfig"] = (
            aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    import aws_sdk_entityresolution.types.id_mapping_techniques

    out["idMappingTechniques"] = (
        aws_sdk_entityresolution.types.id_mapping_techniques.serialize_json(
            value["id_mapping_techniques"]
        )
    )
    if "incremental_run_config" in value:
        import aws_sdk_entityresolution.types.id_mapping_incremental_run_config

        out["incrementalRunConfig"] = (
            aws_sdk_entityresolution.types.id_mapping_incremental_run_config.serialize_json(
                value["incremental_run_config"]
            )
        )
    out["roleArn"] = value.get("role_arn", "")
    return out


def deserialize_json(data: dict) -> UpdateIdMappingWorkflowInput:
    out: UpdateIdMappingWorkflowInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "inputSourceConfig" in data:
        import aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config

        out["input_source_config"] = (
            aws_sdk_entityresolution.types.id_mapping_workflow_input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdMappingWorkflowInput.input_source_config required"
        )
    if "outputSourceConfig" in data:
        import aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config

        out["output_source_config"] = (
            aws_sdk_entityresolution.types.id_mapping_workflow_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    if "idMappingTechniques" in data:
        import aws_sdk_entityresolution.types.id_mapping_techniques

        out["id_mapping_techniques"] = (
            aws_sdk_entityresolution.types.id_mapping_techniques.deserialize_json(
                data["idMappingTechniques"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdMappingWorkflowInput.id_mapping_techniques required"
        )
    if "incrementalRunConfig" in data:
        import aws_sdk_entityresolution.types.id_mapping_incremental_run_config

        out["incremental_run_config"] = (
            aws_sdk_entityresolution.types.id_mapping_incremental_run_config.deserialize_json(
                data["incrementalRunConfig"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
