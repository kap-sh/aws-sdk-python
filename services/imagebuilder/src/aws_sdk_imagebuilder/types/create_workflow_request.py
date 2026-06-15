"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.boolean
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.inline_workflow_data
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.version_number
    import aws_sdk_imagebuilder.types.workflow_type


class CreateWorkflowRequest(TypedDict):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the workflow to create.</p>"""
    semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes the workflow.</p>"""
    change_description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>"""
    data: NotRequired[
        "aws_sdk_imagebuilder.types.inline_workflow_data.InlineWorkflowData"
    ]
    """<p>Contains the UTF-8 encoded YAML document content for the workflow. Alternatively, you can specify the <code>uri</code> of a YAML document file stored in Amazon S3. However, you cannot specify both properties.</p>"""
    uri: NotRequired["aws_sdk_imagebuilder.types.uri.Uri"]
    """<p>The <code>uri</code> of a YAML component document file. This must be an S3 URL (<code>s3://bucket/key</code>), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.</p> <p>Alternatively, you can specify the YAML document inline, using the component <code>data</code> property. You cannot specify both properties.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that apply to the workflow resource.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    type: "aws_sdk_imagebuilder.types.workflow_type.WorkflowType"
    """<p>The phase in the image build process for which the workflow resource is responsible.</p>"""
    dry_run: "aws_sdk_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions for the operation and the request parameters, without actually making the request, and provides an error response. Upon a successful request, the error response is <code>DryRunOperationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "data" in value:
        out["data"] = value["data"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    import aws_sdk_imagebuilder.types.workflow_type

    out["type"] = aws_sdk_imagebuilder.types.workflow_type.serialize_json(value["type"])
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkflowRequest.name required")
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("CreateWorkflowRequest.semantic_version required")
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "data" in data:
        out["data"] = data["data"]
    if "uri" in data:
        out["uri"] = data["uri"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateWorkflowRequest.client_token required")
    if "type" in data:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateWorkflowRequest.type required")
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
