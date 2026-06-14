"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.assistant_integration_configuration
    import aws_sdk_wisdom.types.assistant_status
    import aws_sdk_wisdom.types.assistant_type
    import aws_sdk_wisdom.types.description
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.server_side_encryption_configuration
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid


class AssistantSummary(TypedDict):
    assistant_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the Wisdom assistant.</p>"""
    assistant_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Wisdom assistant.</p>"""
    name: "aws_sdk_wisdom.types.name.Name"
    """<p>The name of the assistant.</p>"""
    type: "aws_sdk_wisdom.types.assistant_type.AssistantType"
    """<p>The type of the assistant.</p>"""
    status: "aws_sdk_wisdom.types.assistant_status.AssistantStatus"
    """<p>The status of the assistant.</p>"""
    description: NotRequired["aws_sdk_wisdom.types.description.Description"]
    """<p>The description of the assistant.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>"""
    integration_configuration: NotRequired[
        "aws_sdk_wisdom.types.assistant_integration_configuration.AssistantIntegrationConfiguration"
    ]
    """<p>The configuration information for the Wisdom assistant integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantSummary) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
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
    if "integration_configuration" in value:
        import aws_sdk_wisdom.types.assistant_integration_configuration

        out["integrationConfiguration"] = (
            aws_sdk_wisdom.types.assistant_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssistantSummary:
    out: AssistantSummary = {}  # type: ignore[typeddict-item]
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantSummary.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantSummary.assistant_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssistantSummary.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssistantSummary.type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AssistantSummary.status required")
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
    if "integrationConfiguration" in data:
        import aws_sdk_wisdom.types.assistant_integration_configuration

        out["integration_configuration"] = (
            aws_sdk_wisdom.types.assistant_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    return out
