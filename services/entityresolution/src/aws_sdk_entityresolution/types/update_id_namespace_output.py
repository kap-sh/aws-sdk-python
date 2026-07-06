"""Generated from Smithy shape ``com.amazonaws.entityresolution#UpdateIdNamespaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.id_namespace_arn
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties_list
    import aws_sdk_entityresolution.types.id_namespace_input_source_config
    import aws_sdk_entityresolution.types.id_namespace_type
    import aws_sdk_entityresolution.types.role_arn


class UpdateIdNamespaceOutput(TypedDict, closed=True):
    id_namespace_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the ID namespace.</p>"""
    id_namespace_arn: "aws_sdk_entityresolution.types.id_namespace_arn.IdNamespaceArn"
    """<p>The Amazon Resource Name (ARN) of the ID namespace.</p>"""
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
    type: "aws_sdk_entityresolution.types.id_namespace_type.IdNamespaceType"
    """<p>The type of ID namespace. There are two types: <code>SOURCE</code> and <code>TARGET</code>.</p> <p>The <code>SOURCE</code> contains configurations for <code>sourceId</code> data that will be processed in an ID mapping workflow. </p> <p>The <code>TARGET</code> contains a configuration of <code>targetId</code> to which all <code>sourceIds</code> will resolve to.</p>"""
    role_arn: NotRequired["aws_sdk_entityresolution.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this <code>IdNamespace</code> on your behalf as part of a workflow run.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdNamespaceOutput) -> dict:
    out: dict = {}
    out["idNamespaceName"] = value["id_namespace_name"]
    out["idNamespaceArn"] = value["id_namespace_arn"]
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
    import aws_sdk_entityresolution.types.id_namespace_type

    out["type"] = aws_sdk_entityresolution.types.id_namespace_type.serialize_json(
        value["type"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["createdAt"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIdNamespaceOutput:
    out: UpdateIdNamespaceOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceName" in data:
        out["id_namespace_name"] = data["idNamespaceName"]
    else:
        raise DeserializationError("UpdateIdNamespaceOutput.id_namespace_name required")
    if "idNamespaceArn" in data:
        out["id_namespace_arn"] = data["idNamespaceArn"]
    else:
        raise DeserializationError("UpdateIdNamespaceOutput.id_namespace_arn required")
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
    if "type" in data:
        import aws_sdk_entityresolution.types.id_namespace_type

        out["type"] = aws_sdk_entityresolution.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("UpdateIdNamespaceOutput.type required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "createdAt" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateIdNamespaceOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateIdNamespaceOutput.updated_at required")
    return out
