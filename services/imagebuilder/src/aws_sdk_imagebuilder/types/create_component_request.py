"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.boolean
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.inline_component_data
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.os_version_list
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.version_number


class CreateComponentRequest(TypedDict, closed=True):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the component.</p>"""
    semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes the contents of the component.</p>"""
    change_description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.</p>"""
    platform: "aws_sdk_imagebuilder.types.platform.Platform"
    """<p>The operating system platform of the component.</p>"""
    supported_os_versions: NotRequired[
        "aws_sdk_imagebuilder.types.os_version_list.OsVersionList"
    ]
    """<p>The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.</p>"""
    data: NotRequired[
        "aws_sdk_imagebuilder.types.inline_component_data.InlineComponentData"
    ]
    """<p>Component <code>data</code> contains inline YAML document content for the component. Alternatively, you can specify the <code>uri</code> of a YAML document file stored in Amazon S3. However, you cannot specify both properties.</p>"""
    uri: NotRequired["aws_sdk_imagebuilder.types.uri.Uri"]
    """<p>The <code>uri</code> of a YAML component document file. This must be an S3 URL (<code>s3://bucket/key</code>), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.</p> <p>Alternatively, you can specify the YAML document inline, using the component <code>data</code> property. You cannot specify both properties.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to the component.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "aws_sdk_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions for the operation and the request parameters, without actually making the request, and provides an error response. Upon a successful request, the error response is <code>DryRunOperationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    import aws_sdk_imagebuilder.types.platform

    out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
        value["platform"]
    )
    if "supported_os_versions" in value:
        import aws_sdk_imagebuilder.types.os_version_list

        out["supportedOsVersions"] = (
            aws_sdk_imagebuilder.types.os_version_list.serialize_json(
                value["supported_os_versions"]
            )
        )
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
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateComponentRequest:
    out: CreateComponentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateComponentRequest.name required")
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("CreateComponentRequest.semantic_version required")
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("CreateComponentRequest.platform required")
    if "supportedOsVersions" in data:
        import aws_sdk_imagebuilder.types.os_version_list

        out["supported_os_versions"] = (
            aws_sdk_imagebuilder.types.os_version_list.deserialize_json(
                data["supportedOsVersions"]
            )
        )
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
        raise DeserializationError("CreateComponentRequest.client_token required")
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
