"""Generated from Smithy shape ``com.amazonaws.entityresolution#UpdateIdNamespaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list
    import aws_sdk_entityresolution.types.id_namespace_input_source_config
    import aws_sdk_entityresolution.types.role_arn


class UpdateIdNamespaceInput(TypedDict, closed=True):
    id_namespace_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the ID namespace.</p>"""
    description: NotRequired["aws_sdk_entityresolution.types.description.Description"]
    """<p>The description of the ID namespace.</p>"""
    input_source_config: NotRequired[
        "aws_sdk_entityresolution.types.id_namespace_input_source_config.IdNamespaceInputSourceConfig"
    ]
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    id_mapping_workflow_properties: NotRequired[
        "aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.IdNamespaceIdMappingWorkflowPropertiesList"
    ]
    """<p>Determines the properties of <code>IdMappingWorkflow</code> where this <code>IdNamespace</code> can be used as a <code>Source</code> or a <code>Target</code>.</p>"""
    role_arn: NotRequired["aws_sdk_entityresolution.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this <code>IdNamespace</code> on your behalf as part of a workflow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdNamespaceInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "input_source_config" in value:
        import aws_sdk_entityresolution.types.id_namespace_input_source_config

        out["inputSourceConfig"] = (
            aws_sdk_entityresolution.types.id_namespace_input_source_config.serialize_json(
                value["input_source_config"]
            )
        )
    if "id_mapping_workflow_properties" in value:
        import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list

        out["idMappingWorkflowProperties"] = (
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.serialize_json(
                value["id_mapping_workflow_properties"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateIdNamespaceInput:
    out: UpdateIdNamespaceInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "inputSourceConfig" in data:
        import aws_sdk_entityresolution.types.id_namespace_input_source_config

        out["input_source_config"] = (
            aws_sdk_entityresolution.types.id_namespace_input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    if "idMappingWorkflowProperties" in data:
        import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list

        out["id_mapping_workflow_properties"] = (
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.deserialize_json(
                data["idMappingWorkflowProperties"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
