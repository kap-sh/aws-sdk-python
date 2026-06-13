"""Generated from Smithy shape ``com.amazonaws.omics#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

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
    import aws_sdk_omics.types.workflow_description
    import aws_sdk_omics.types.workflow_engine
    import aws_sdk_omics.types.workflow_main
    import aws_sdk_omics.types.workflow_name
    import aws_sdk_omics.types.workflow_parameter_template
    import aws_sdk_omics.types.workflow_request_id


class CreateWorkflowRequest(TypedDict):
    name: NotRequired["aws_sdk_omics.types.workflow_name.WorkflowName"]
    """<p>Name (optional but highly recommended) for the workflow to locate relevant information in the CloudWatch logs and Amazon Web Services HealthOmics console. </p>"""
    description: NotRequired[
        "aws_sdk_omics.types.workflow_description.WorkflowDescription"
    ]
    """<p>A description for the workflow.</p>"""
    engine: NotRequired["aws_sdk_omics.types.workflow_engine.WorkflowEngine"]
    """<p>The workflow engine for the workflow. By default, Amazon Web Services HealthOmics detects the engine automatically from your workflow definition. Provide a value if you have workflow definition files from more than one engine in your zip file, or to use WDL lenient.</p> <p>WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell directives and some non-conformant logic. For details, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflow-wdl-type-conversion.html\">Implicit type conversion in WDL lenient</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    definition_zip: NotRequired["bytes"]
    """<p>A ZIP archive containing the main workflow definition file and dependencies that it imports for the workflow. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html\">Workflow definition requirements</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    definition_uri: NotRequired[
        "aws_sdk_omics.types.workflow_definition.WorkflowDefinition"
    ]
    """<p>The S3 URI of a definition for the workflow. The S3 bucket must be in the same region as the workflow.</p>"""
    main: NotRequired["aws_sdk_omics.types.workflow_main.WorkflowMain"]
    """<p>The path of the main definition file for the workflow. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>"""
    parameter_template: NotRequired[
        "aws_sdk_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
    ]
    """<p>A parameter template for the workflow. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html\">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the workflow. You can define up to 50 tags for the workflow. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html\">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    request_id: "aws_sdk_omics.types.workflow_request_id.WorkflowRequestId"
    """<p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>"""
    accelerators: NotRequired["aws_sdk_omics.types.accelerators.Accelerators"]
    """<p>The computational accelerator specified to run the workflow.</p>"""
    storage_type: NotRequired["aws_sdk_omics.types.storage_type.StorageType"]
    """<p>The default storage type for runs that use this workflow. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. <code>STATIC</code> storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html\">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    container_registry_map: NotRequired[
        "aws_sdk_omics.types.container_registry_map.ContainerRegistryMap"
    ]
    """<p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html\">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    container_registry_map_uri: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>(Optional) URI of the S3 location for the registry mapping file.</p>"""
    readme_markdown: NotRequired["aws_sdk_omics.types.readme_markdown.ReadmeMarkdown"]
    """<p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>"""
    parameter_template_path: NotRequired[
        "aws_sdk_omics.types.parameter_template_path.ParameterTemplatePath"
    ]
    """<p>The path to the workflow parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow. If not specified, the workflow will be created without a parameter template.</p>"""
    readme_path: NotRequired["aws_sdk_omics.types.readme_path.ReadmePath"]
    """<p>The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>"""
    definition_repository: NotRequired[
        "aws_sdk_omics.types.definition_repository.DefinitionRepository"
    ]
    """<p>The repository information for the workflow definition. This allows you to source your workflow definition directly from a code repository.</p>"""
    workflow_bucket_owner_id: NotRequired[
        "aws_sdk_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
    ]
    """<p>The Amazon Web Services account ID of the expected owner of the S3 bucket that contains the workflow definition. If not specified, the service skips the validation.</p>"""
    readme_uri: NotRequired["aws_sdk_omics.types.s3_uri_for_object.S3UriForObject"]
    """<p>The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "definition_zip" in value:
        import aws_sdk_omics.types._prelude.blob

        out["definitionZip"] = aws_sdk_omics.types._prelude.blob.serialize_json(
            value["definition_zip"]
        )
    if "definition_uri" in value:
        out["definitionUri"] = value["definition_uri"]
    if "main" in value:
        out["main"] = value["main"]
    if "parameter_template" in value:
        import aws_sdk_omics.types.workflow_parameter_template

        out["parameterTemplate"] = (
            aws_sdk_omics.types.workflow_parameter_template.serialize_json(
                value["parameter_template"]
            )
        )
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    if "accelerators" in value:
        out["accelerators"] = value["accelerators"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
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
    if "workflow_bucket_owner_id" in value:
        out["workflowBucketOwnerId"] = value["workflow_bucket_owner_id"]
    if "readme_uri" in value:
        out["readmeUri"] = value["readme_uri"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "engine" in data:
        out["engine"] = data["engine"]
    if "definitionZip" in data:
        import aws_sdk_omics.types._prelude.blob

        out["definition_zip"] = aws_sdk_omics.types._prelude.blob.deserialize_json(
            data["definitionZip"]
        )
    if "definitionUri" in data:
        out["definition_uri"] = data["definitionUri"]
    if "main" in data:
        out["main"] = data["main"]
    if "parameterTemplate" in data:
        import aws_sdk_omics.types.workflow_parameter_template

        out["parameter_template"] = (
            aws_sdk_omics.types.workflow_parameter_template.deserialize_json(
                data["parameterTemplate"]
            )
        )
    if "storageCapacity" in data:
        out["storage_capacity"] = data["storageCapacity"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("CreateWorkflowRequest.request_id required")
    if "accelerators" in data:
        out["accelerators"] = data["accelerators"]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
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
    if "workflowBucketOwnerId" in data:
        out["workflow_bucket_owner_id"] = data["workflowBucketOwnerId"]
    if "readmeUri" in data:
        out["readme_uri"] = data["readmeUri"]
    return out
