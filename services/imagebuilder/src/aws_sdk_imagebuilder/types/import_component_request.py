"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.component_format
    import aws_sdk_imagebuilder.types.component_type
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.version_number


class ImportComponentRequest(TypedDict, closed=True):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the component.</p>"""
    semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the component. Describes the contents of the component.</p>"""
    change_description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The change description of the component. This description indicates the change that has been made in this version, or what makes this version different from other versions of the component.</p>"""
    type: "aws_sdk_imagebuilder.types.component_type.ComponentType"
    """<p>The type of the component denotes whether the component is used to build the image, or only to test it.</p>"""
    format: "aws_sdk_imagebuilder.types.component_format.ComponentFormat"
    """<p>The format of the resource that you want to import as a component.</p>"""
    platform: "aws_sdk_imagebuilder.types.platform.Platform"
    """<p>The platform of the component.</p>"""
    data: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The data of the component. Used to specify the data inline. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>"""
    uri: NotRequired["aws_sdk_imagebuilder.types.uri.Uri"]
    """<p>The uri of the component. Must be an Amazon S3 URL and the requester must have permission to access the Amazon S3 bucket. If you use Amazon S3, you can specify component content up to your service quota. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the component.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportComponentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    import aws_sdk_imagebuilder.types.component_type

    out["type"] = aws_sdk_imagebuilder.types.component_type.serialize_json(
        value["type"]
    )
    import aws_sdk_imagebuilder.types.component_format

    out["format"] = aws_sdk_imagebuilder.types.component_format.serialize_json(
        value["format"]
    )
    import aws_sdk_imagebuilder.types.platform

    out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
        value["platform"]
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
    return out


def deserialize_json(data: dict) -> ImportComponentRequest:
    out: ImportComponentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportComponentRequest.name required")
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportComponentRequest.semantic_version required")
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "type" in data:
        import aws_sdk_imagebuilder.types.component_type

        out["type"] = aws_sdk_imagebuilder.types.component_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.type required")
    if "format" in data:
        import aws_sdk_imagebuilder.types.component_format

        out["format"] = aws_sdk_imagebuilder.types.component_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.format required")
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.platform required")
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
        raise DeserializationError("ImportComponentRequest.client_token required")
    return out
