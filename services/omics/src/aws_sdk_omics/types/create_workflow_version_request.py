"""Generated from Smithy shape ``com.amazonaws.omics#CreateWorkflowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.accelerators
    import aws_sdk_omics.types.container_registry_map
    import aws_sdk_omics.types.definition_repository
    import aws_sdk_omics.types.parameter_template_path
    import aws_sdk_omics.types.readme_markdown
    import aws_sdk_omics.types.readme_path
    import aws_sdk_omics.types.s3_uri_for_object
    import aws_sdk_omics.types.storage_type
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.uri
    import aws_sdk_omics.types.workflow_bucket_owner_id
    import aws_sdk_omics.types.workflow_definition
    import aws_sdk_omics.types.workflow_engine
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_main
    import aws_sdk_omics.types.workflow_parameter_template
    import aws_sdk_omics.types.workflow_request_id
    import aws_sdk_omics.types.workflow_version_description
    import aws_sdk_omics.types.workflow_version_name


class CreateWorkflowVersionRequest(TypedDict, closed=True):
    workflow_id: "aws_sdk_omics.types.workflow_id.WorkflowId"
    """<p>The ID of the workflow where you are creating the new version. The <code>workflowId</code> is not the UUID.</p>"""
    version_name: "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    """<p>A name for the workflow version. Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version. </p> <p>The version name must start with a letter or number and it can include upper-case and lower-case letters, numbers, hyphens, periods and underscores. The maximum length is 64 characters. You can use a simple naming scheme, such as version1, version2, version3. You can also match your workflow versions with your own internal versioning conventions, such as 2.7.0, 2.7.1, 2.7.2.</p>"""
    definition_zip: NotRequired["bytes"]
    """<p>A ZIP archive containing the main workflow definition file and dependencies that it imports for this workflow version. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see Workflow definition requirements in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    definition_uri: NotRequired[
        "aws_sdk_omics.types.workflow_definition.WorkflowDefinition"
    ]
    """<p>The S3 URI of a definition for this workflow version. The S3 bucket must be in the same region as this workflow version.</p>"""
    accelerators: NotRequired["aws_sdk_omics.types.accelerators.Accelerators"]
    """<p>The computational accelerator for this workflow version.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.workflow_version_description.WorkflowVersionDescription"
    ]
    """<p>A description for this workflow version.</p>"""
    engine: NotRequired["aws_sdk_omics.types.workflow_engine.WorkflowEngine"]
    """<p>The workflow engine for this workflow version. This is only required if you have workflow definition files from more than one engine in your zip file. Otherwise, the service can detect the engine automatically from your workflow definition.</p>"""
    main: NotRequired["aws_sdk_omics.types.workflow_main.WorkflowMain"]
    """<p>The path of the main definition file for this workflow version. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>"""
    parameter_template: NotRequired[
        "aws_sdk_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
    ]
    r"""<p>A parameter template for this workflow version. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html\">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    request_id: "aws_sdk_omics.types.workflow_request_id.WorkflowRequestId"
    """<p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>"""
    storage_type: NotRequired["aws_sdk_omics.types.storage_type.StorageType"]
    r"""<p>The default storage type for runs that use this workflow version. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html\">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The default static storage capacity (in gibibytes) for runs that use this workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    r"""<p>Tags for this workflow version. You can define up to 50 tags for the workflow. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html\">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    workflow_bucket_owner_id: NotRequired[
        "aws_sdk_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
    ]
    """<p>Amazon Web Services Id of the owner of the S3 bucket that contains the workflow definition. You need to specify this parameter if your account is not the bucket owner.</p>"""
    container_registry_map: NotRequired[
        "aws_sdk_omics.types.container_registry_map.ContainerRegistryMap"
    ]
    r"""<p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html\">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    container_registry_map_uri: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>(Optional) URI of the S3 location for the registry mapping file.</p>"""
    readme_markdown: NotRequired["aws_sdk_omics.types.readme_markdown.ReadmeMarkdown"]
    """<p>The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.</p>"""
    parameter_template_path: NotRequired[
        "aws_sdk_omics.types.parameter_template_path.ParameterTemplatePath"
    ]
    """<p>The path to the workflow version parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow version. If not specified, the workflow version will be created without a parameter template.</p>"""
    readme_path: NotRequired["aws_sdk_omics.types.readme_path.ReadmePath"]
    """<p>The path to the workflow version README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>"""
    definition_repository: NotRequired[
        "aws_sdk_omics.types.definition_repository.DefinitionRepository"
    ]
    """<p>The repository information for the workflow version definition. This allows you to source your workflow version definition directly from a code repository.</p>"""
    readme_uri: NotRequired["aws_sdk_omics.types.s3_uri_for_object.S3UriForObject"]
    """<p>The S3 URI of the README file for the workflow version. This file provides documentation and usage information for the workflow version. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowVersionRequest) -> dict:
    out: dict = {}
    out["versionName"] = value["version_name"]
    if "definition_zip" in value:
        import aws_sdk_omics.types._prelude.blob

        out["definitionZip"] = aws_sdk_omics.types._prelude.blob.serialize_json(
            value["definition_zip"]
        )
    if "definition_uri" in value:
        out["definitionUri"] = value["definition_uri"]
    if "accelerators" in value:
        out["accelerators"] = value["accelerators"]
    if "description" in value:
        out["description"] = value["description"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "main" in value:
        out["main"] = value["main"]
    if "parameter_template" in value:
        import aws_sdk_omics.types.workflow_parameter_template

        out["parameterTemplate"] = (
            aws_sdk_omics.types.workflow_parameter_template.serialize_json(
                value["parameter_template"]
            )
        )
    out["requestId"] = value["request_id"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "workflow_bucket_owner_id" in value:
        out["workflowBucketOwnerId"] = value["workflow_bucket_owner_id"]
    if "container_registry_map" in value:
        import aws_sdk_omics.types.container_registry_map

        out["containerRegistryMap"] = (
            aws_sdk_omics.types.container_registry_map.serialize_json(
                value["container_registry_map"]
            )
        )
    if "container_registry_map_uri" in value:
        out["containerRegistryMapUri"] = value["container_registry_map_uri"]
    if "readme_markdown" in value:
        out["readmeMarkdown"] = value["readme_markdown"]
    if "parameter_template_path" in value:
        out["parameterTemplatePath"] = value["parameter_template_path"]
    if "readme_path" in value:
        out["readmePath"] = value["readme_path"]
    if "definition_repository" in value:
        import aws_sdk_omics.types.definition_repository

        out["definitionRepository"] = (
            aws_sdk_omics.types.definition_repository.serialize_json(
                value["definition_repository"]
            )
        )
    if "readme_uri" in value:
        out["readmeUri"] = value["readme_uri"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowVersionRequest:
    out: CreateWorkflowVersionRequest = {}  # type: ignore[typeddict-item]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError("CreateWorkflowVersionRequest.version_name required")
    if "definitionZip" in data:
        import aws_sdk_omics.types._prelude.blob

        out["definition_zip"] = aws_sdk_omics.types._prelude.blob.deserialize_json(
            data["definitionZip"]
        )
    if "definitionUri" in data:
        out["definition_uri"] = data["definitionUri"]
    if "accelerators" in data:
        out["accelerators"] = data["accelerators"]
    if "description" in data:
        out["description"] = data["description"]
    if "engine" in data:
        out["engine"] = data["engine"]
    if "main" in data:
        out["main"] = data["main"]
    if "parameterTemplate" in data:
        import aws_sdk_omics.types.workflow_parameter_template

        out["parameter_template"] = (
            aws_sdk_omics.types.workflow_parameter_template.deserialize_json(
                data["parameterTemplate"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("CreateWorkflowVersionRequest.request_id required")
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "storageCapacity" in data:
        out["storage_capacity"] = data["storageCapacity"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "workflowBucketOwnerId" in data:
        out["workflow_bucket_owner_id"] = data["workflowBucketOwnerId"]
    if "containerRegistryMap" in data:
        import aws_sdk_omics.types.container_registry_map

        out["container_registry_map"] = (
            aws_sdk_omics.types.container_registry_map.deserialize_json(
                data["containerRegistryMap"]
            )
        )
    if "containerRegistryMapUri" in data:
        out["container_registry_map_uri"] = data["containerRegistryMapUri"]
    if "readmeMarkdown" in data:
        out["readme_markdown"] = data["readmeMarkdown"]
    if "parameterTemplatePath" in data:
        out["parameter_template_path"] = data["parameterTemplatePath"]
    if "readmePath" in data:
        out["readme_path"] = data["readmePath"]
    if "definitionRepository" in data:
        import aws_sdk_omics.types.definition_repository

        out["definition_repository"] = (
            aws_sdk_omics.types.definition_repository.deserialize_json(
                data["definitionRepository"]
            )
        )
    if "readmeUri" in data:
        out["readme_uri"] = data["readmeUri"]
    return out
