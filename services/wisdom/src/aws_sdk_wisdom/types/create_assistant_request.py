"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateAssistantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.assistant_type
    import aws_sdk_wisdom.types.client_token
    import aws_sdk_wisdom.types.description
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.server_side_encryption_configuration
    import aws_sdk_wisdom.types.tags


class CreateAssistantRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_wisdom.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    name: "aws_sdk_wisdom.types.name.Name"
    """<p>The name of the assistant.</p>"""
    type: "aws_sdk_wisdom.types.assistant_type.AssistantType"
    """<p>The type of assistant.</p>"""
    description: NotRequired["aws_sdk_wisdom.types.description.Description"]
    """<p>The description of the assistant.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    if "server_side_encryption_configuration" in value:
        import aws_sdk_wisdom.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            aws_sdk_wisdom.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssistantRequest:
    out: CreateAssistantRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssistantRequest.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAssistantRequest.type required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    if "serverSideEncryptionConfiguration" in data:
        import aws_sdk_wisdom.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_wisdom.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    return out
