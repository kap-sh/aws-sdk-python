"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.assistant_association_output_data
    import capo_qconnect.types.association_type
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class AssistantAssociationData(TypedDict, closed=True):
    assistant_association_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association.</p>"""
    assistant_association_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the assistant association.</p>"""
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    association_type: "capo_qconnect.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association_data: "capo_qconnect.types.assistant_association_output_data.AssistantAssociationOutputData"
    """<p>A union type that currently has a single argument, the knowledge base ID.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationData) -> dict:
    out: dict = {}
    out["assistantAssociationId"] = value["assistant_association_id"]
    out["assistantAssociationArn"] = value["assistant_association_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["associationType"] = value["association_type"]
    import capo_qconnect.types.assistant_association_output_data

    out["associationData"] = (
        capo_qconnect.types.assistant_association_output_data.serialize_json(
            value["association_data"]
        )
    )
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssistantAssociationData:
    out: AssistantAssociationData = {}  # type: ignore[typeddict-item]
    if "assistantAssociationId" in data:
        out["assistant_association_id"] = data["assistantAssociationId"]
    else:
        raise DeserializationError(
            "AssistantAssociationData.assistant_association_id required"
        )
    if "assistantAssociationArn" in data:
        out["assistant_association_arn"] = data["assistantAssociationArn"]
    else:
        raise DeserializationError(
            "AssistantAssociationData.assistant_association_arn required"
        )
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
        import capo_qconnect.types.assistant_association_output_data

        out["association_data"] = (
            capo_qconnect.types.assistant_association_output_data.deserialize_json(
                data["associationData"]
            )
        )
    else:
        raise DeserializationError("AssistantAssociationData.association_data required")
    if "tags" in data:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
