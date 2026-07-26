"""Generated from Smithy shape ``com.amazonaws.omics#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.accelerators
    import capo_omics.types.container_registry_map
    import capo_omics.types.definition_repository_details
    import capo_omics.types.readme_path
    import capo_omics.types.readme_s3_presigned_url
    import capo_omics.types.storage_type
    import capo_omics.types.tag_map
    import capo_omics.types.workflow_arn
    import capo_omics.types.workflow_definition
    import capo_omics.types.workflow_description
    import capo_omics.types.workflow_digest
    import capo_omics.types.workflow_engine
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_main
    import capo_omics.types.workflow_metadata
    import capo_omics.types.workflow_name
    import capo_omics.types.workflow_parameter_template
    import capo_omics.types.workflow_profile_list
    import capo_omics.types.workflow_profile_parameter_templates
    import capo_omics.types.workflow_status
    import capo_omics.types.workflow_status_message
    import capo_omics.types.workflow_timestamp
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_uuid


class GetWorkflowResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.workflow_arn.WorkflowArn"]
    """<p>The workflow's ARN.</p>"""
    id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    status: NotRequired["capo_omics.types.workflow_status.WorkflowStatus"]
    """<p>The workflow's status.</p>"""
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow's type.</p>"""
    name: NotRequired["capo_omics.types.workflow_name.WorkflowName"]
    """<p>The workflow's name.</p>"""
    description: NotRequired[
        "capo_omics.types.workflow_description.WorkflowDescription"
    ]
    """<p>The workflow's description.</p>"""
    engine: NotRequired["capo_omics.types.workflow_engine.WorkflowEngine"]
    """<p>The workflow's engine.</p>"""
    definition: NotRequired["capo_omics.types.workflow_definition.WorkflowDefinition"]
    """<p>The workflow's definition.</p>"""
    main: NotRequired["capo_omics.types.workflow_main.WorkflowMain"]
    """<p>The path of the main definition file for the workflow.</p>"""
    digest: NotRequired["capo_omics.types.workflow_digest.WorkflowDigest"]
    """<p>The workflow's digest.</p>"""
    parameter_template: NotRequired[
        "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
    ]
    """<p>The workflow's parameter template.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.</p>"""
    creation_time: NotRequired["capo_omics.types.workflow_timestamp.WorkflowTimestamp"]
    """<p>When the workflow was created.</p>"""
    status_message: NotRequired[
        "capo_omics.types.workflow_status_message.WorkflowStatusMessage"
    ]
    """<p>The workflow's status message.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The workflow's tags.</p>"""
    metadata: NotRequired["capo_omics.types.workflow_metadata.WorkflowMetadata"]
    """<p>Gets metadata for the workflow.</p>"""
    accelerators: NotRequired["capo_omics.types.accelerators.Accelerators"]
    """<p>The computational accelerator specified to run the workflow. </p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The default storage type for runs using this workflow.</p>"""
    uuid: NotRequired["capo_omics.types.workflow_uuid.WorkflowUuid"]
    """<p>The universally unique identifier (UUID) value for this workflow.</p>"""
    container_registry_map: NotRequired[
        "capo_omics.types.container_registry_map.ContainerRegistryMap"
    ]
    """<p>The registry map that this workflow is using.</p>"""
    readme: NotRequired["capo_omics.types.readme_s3_presigned_url.ReadmeS3PresignedUrl"]
    """<p>The README content for the workflow, providing documentation and usage information.</p>"""
    definition_repository_details: NotRequired[
        "capo_omics.types.definition_repository_details.DefinitionRepositoryDetails"
    ]
    """<p>Details about the source code repository that hosts the workflow definition files.</p>"""
    readme_path: NotRequired["capo_omics.types.readme_path.ReadmePath"]
    """<p>The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>"""
    profiles: NotRequired["capo_omics.types.workflow_profile_list.WorkflowProfileList"]
    """<p>The list of Nextflow profiles that are available for this workflow. Profiles allow you to select predefined configuration settings at runtime.</p>"""
    profile_parameter_templates: NotRequired[
        "capo_omics.types.workflow_profile_parameter_templates.WorkflowProfileParameterTemplates"
    ]
    """<p>A mapping of profile names to their parameter templates. Each profile defines its own set of parameters that you can use when starting a run with that profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "main" in value:
        out["main"] = value["main"]
    if "digest" in value:
        out["digest"] = value["digest"]
    if "parameter_template" in value:
        import capo_omics.types.workflow_parameter_template

        out["parameterTemplate"] = (
            capo_omics.types.workflow_parameter_template.serialize_json(
                value["parameter_template"]
            )
        )
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "creation_time" in value:
        import capo_omics.types.workflow_timestamp

        out["creationTime"] = capo_omics.types.workflow_timestamp.serialize_json(
            value["creation_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "metadata" in value:
        import capo_omics.types.workflow_metadata

        out["metadata"] = capo_omics.types.workflow_metadata.serialize_json(
            value["metadata"]
        )
    if "accelerators" in value:
        out["accelerators"] = value["accelerators"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "container_registry_map" in value:
        import capo_omics.types.container_registry_map

        out["containerRegistryMap"] = (
            capo_omics.types.container_registry_map.serialize_json(
                value["container_registry_map"]
            )
        )
    if "readme" in value:
        out["readme"] = value["readme"]
    if "definition_repository_details" in value:
        import capo_omics.types.definition_repository_details

        out["definitionRepositoryDetails"] = (
            capo_omics.types.definition_repository_details.serialize_json(
                value["definition_repository_details"]
            )
        )
    if "readme_path" in value:
        out["readmePath"] = value["readme_path"]
    if "profiles" in value:
        import capo_omics.types.workflow_profile_list

        out["profiles"] = capo_omics.types.workflow_profile_list.serialize_json(
            value["profiles"]
        )
    if "profile_parameter_templates" in value:
        import capo_omics.types.workflow_profile_parameter_templates

        out["profileParameterTemplates"] = (
            capo_omics.types.workflow_profile_parameter_templates.serialize_json(
                value["profile_parameter_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "engine" in data:
        out["engine"] = data["engine"]
    if "definition" in data:
        out["definition"] = data["definition"]
    if "main" in data:
        out["main"] = data["main"]
    if "digest" in data:
        out["digest"] = data["digest"]
    if "parameterTemplate" in data:
        import capo_omics.types.workflow_parameter_template

        out["parameter_template"] = (
            capo_omics.types.workflow_parameter_template.deserialize_json(
                data["parameterTemplate"]
            )
        )
    if "storageCapacity" in data:
        out["storage_capacity"] = data["storageCapacity"]
    if "creationTime" in data:
        import capo_omics.types.workflow_timestamp

        out["creation_time"] = capo_omics.types.workflow_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if "metadata" in data:
        import capo_omics.types.workflow_metadata

        out["metadata"] = capo_omics.types.workflow_metadata.deserialize_json(
            data["metadata"]
        )
    if "accelerators" in data:
        out["accelerators"] = data["accelerators"]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "containerRegistryMap" in data:
        import capo_omics.types.container_registry_map

        out["container_registry_map"] = (
            capo_omics.types.container_registry_map.deserialize_json(
                data["containerRegistryMap"]
            )
        )
    if "readme" in data:
        out["readme"] = data["readme"]
    if "definitionRepositoryDetails" in data:
        import capo_omics.types.definition_repository_details

        out["definition_repository_details"] = (
            capo_omics.types.definition_repository_details.deserialize_json(
                data["definitionRepositoryDetails"]
            )
        )
    if "readmePath" in data:
        out["readme_path"] = data["readmePath"]
    if "profiles" in data:
        import capo_omics.types.workflow_profile_list

        out["profiles"] = capo_omics.types.workflow_profile_list.deserialize_json(
            data["profiles"]
        )
    if "profileParameterTemplates" in data:
        import capo_omics.types.workflow_profile_parameter_templates

        out["profile_parameter_templates"] = (
            capo_omics.types.workflow_profile_parameter_templates.deserialize_json(
                data["profileParameterTemplates"]
            )
        )
    return out
