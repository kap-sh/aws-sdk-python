"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_wisdom.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.assistant_association_output_data
    import aws_sdk_wisdom.types.association_type
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid

class AssistantAssociationData(TypedDict):
    assistant_association_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the assistant association.</p>"""
    assistant_association_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the assistant association.</p>"""
    assistant_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the Wisdom assistant.</p>"""
    assistant_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Wisdom assistant.</p>"""
    association_type: "aws_sdk_wisdom.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association_data: "aws_sdk_wisdom.types.assistant_association_output_data.AssistantAssociationOutputData"
    """<p>A union type that currently has a single argument, the knowledge base ID.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationData) -> dict:
    out: dict = {}
    out["assistantAssociationId"] = value["assistant_association_id"]
    out["assistantAssociationArn"] = value["assistant_association_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["associationType"] = value["association_type"]
    import aws_sdk_wisdom.types.assistant_association_output_data
    out["associationData"] = aws_sdk_wisdom.types.assistant_association_output_data.serialize_json(value["association_data"])
    if "tags" in value:
        import aws_sdk_wisdom.types.tags
        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssistantAssociationData:
    out: AssistantAssociationData = {}  # type: ignore[typeddict-item]
    if "assistantAssociationId" in data:
        out["assistant_association_id"] = data["assistantAssociationId"]
    else:
        raise DeserializationError("AssistantAssociationData.assistant_association_id required")
    if "assistantAssociationArn" in data:
        out["assistant_association_arn"] = data["assistantAssociationArn"]
    else:
        raise DeserializationError("AssistantAssociationData.assistant_association_arn required")
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantAssociationData.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantAssociationData.assistant_arn required")
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError("AssistantAssociationData.association_type required")
    if "associationData" in data:
        import aws_sdk_wisdom.types.assistant_association_output_data
        out["association_data"] = aws_sdk_wisdom.types.assistant_association_output_data.deserialize_json(data["associationData"])
    else:
        raise DeserializationError("AssistantAssociationData.association_data required")
    if "tags" in data:
        import aws_sdk_wisdom.types.tags
        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    return out