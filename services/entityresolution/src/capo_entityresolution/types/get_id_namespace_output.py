"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdNamespaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.id_namespace_arn
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list
    import capo_entityresolution.types.id_namespace_input_source_config
    import capo_entityresolution.types.id_namespace_type
    import capo_entityresolution.types.role_arn
    import capo_entityresolution.types.tag_map


class GetIdNamespaceOutput(TypedDict, closed=True):
    id_namespace_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the ID namespace.</p>"""
    id_namespace_arn: "capo_entityresolution.types.id_namespace_arn.IdNamespaceArn"
    """<p>The Amazon Resource Name (ARN) of the ID namespace.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>The description of the ID namespace.</p>"""
    input_source_config: NotRequired[
        "capo_entityresolution.types.id_namespace_input_source_config.IdNamespaceInputSourceConfig"
    ]
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    id_mapping_workflow_properties: NotRequired[
        "capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.IdNamespaceIdMappingWorkflowPropertiesList"
    ]
    """<p>Determines the properties of <code>IdMappingWorkflow</code> where this <code>IdNamespace</code> can be used as a <code>Source</code> or a <code>Target</code>.</p>"""
    type: "capo_entityresolution.types.id_namespace_type.IdNamespaceType"
    """<p>The type of ID namespace. There are two types: <code>SOURCE</code> and <code>TARGET</code>.</p> <p>The <code>SOURCE</code> contains configurations for <code>sourceId</code> data that will be processed in an ID mapping workflow. </p> <p>The <code>TARGET</code> contains a configuration of <code>targetId</code> to which all <code>sourceIds</code> will resolve to.</p>"""
    role_arn: NotRequired["capo_entityresolution.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this <code>IdNamespace</code> on your behalf as part of a workflow run.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was last updated.</p>"""
    tags: NotRequired["capo_entityresolution.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdNamespaceOutput) -> dict:
    out: dict = {}
    out["idNamespaceName"] = value["id_namespace_name"]
    out["idNamespaceArn"] = value["id_namespace_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "input_source_config" in value:
        import capo_entityresolution.types.id_namespace_input_source_config

        out["inputSourceConfig"] = (
            capo_entityresolution.types.id_namespace_input_source_config.serialize_json(
                value["input_source_config"]
            )
        )
    if "id_mapping_workflow_properties" in value:
        import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list

        out["idMappingWorkflowProperties"] = (
            capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.serialize_json(
                value["id_mapping_workflow_properties"]
            )
        )
    import capo_entityresolution.types.id_namespace_type

    out["type"] = capo_entityresolution.types.id_namespace_type.serialize_json(
        value["type"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetIdNamespaceOutput:
    out: GetIdNamespaceOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceName" in data:
        out["id_namespace_name"] = data["idNamespaceName"]
    else:
        raise DeserializationError("GetIdNamespaceOutput.id_namespace_name required")
    if "idNamespaceArn" in data:
        out["id_namespace_arn"] = data["idNamespaceArn"]
    else:
        raise DeserializationError("GetIdNamespaceOutput.id_namespace_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "inputSourceConfig" in data:
        import capo_entityresolution.types.id_namespace_input_source_config

        out["input_source_config"] = (
            capo_entityresolution.types.id_namespace_input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    if "idMappingWorkflowProperties" in data:
        import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list

        out["id_mapping_workflow_properties"] = (
            capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.deserialize_json(
                data["idMappingWorkflowProperties"]
            )
        )
    if "type" in data:
        import capo_entityresolution.types.id_namespace_type

        out["type"] = capo_entityresolution.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetIdNamespaceOutput.type required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "createdAt" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetIdNamespaceOutput.created_at required")
    if "updatedAt" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetIdNamespaceOutput.updated_at required")
    if "tags" in data:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    return out
