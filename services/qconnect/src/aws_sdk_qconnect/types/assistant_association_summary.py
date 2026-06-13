"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.assistant_association_output_data
    import aws_sdk_qconnect.types.association_type
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid


class AssistantAssociationSummary(TypedDict):
    assistant_association_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association.</p>"""
    assistant_association_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the assistant association.</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    association_type: "aws_sdk_qconnect.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association_data: "aws_sdk_qconnect.types.assistant_association_output_data.AssistantAssociationOutputData"
    """<p>The association data.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationSummary) -> dict:
    out: dict = {}
    out["assistantAssociationId"] = value["assistant_association_id"]
    out["assistantAssociationArn"] = value["assistant_association_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["associationType"] = value["association_type"]
    import aws_sdk_qconnect.types.assistant_association_output_data

    out["associationData"] = (
        aws_sdk_qconnect.types.assistant_association_output_data.serialize_json(
            value["association_data"]
        )
    )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssistantAssociationSummary:
    out: AssistantAssociationSummary = {}  # type: ignore[typeddict-item]
    if "assistantAssociationId" in data:
        out["assistant_association_id"] = data["assistantAssociationId"]
    else:
        raise DeserializationError(
            "AssistantAssociationSummary.assistant_association_id required"
        )
    if "assistantAssociationArn" in data:
        out["assistant_association_arn"] = data["assistantAssociationArn"]
    else:
        raise DeserializationError(
            "AssistantAssociationSummary.assistant_association_arn required"
        )
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantAssociationSummary.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantAssociationSummary.assistant_arn required")
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError(
            "AssistantAssociationSummary.association_type required"
        )
    if "associationData" in data:
        import aws_sdk_qconnect.types.assistant_association_output_data

        out["association_data"] = (
            aws_sdk_qconnect.types.assistant_association_output_data.deserialize_json(
                data["associationData"]
            )
        )
    else:
        raise DeserializationError(
            "AssistantAssociationSummary.association_data required"
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
