"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.assistant_association_output_data
    import capo_wisdom.types.association_type
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class AssistantAssociationSummary(TypedDict, closed=True):
    assistant_association_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the assistant association.</p>"""
    assistant_association_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the assistant association.</p>"""
    assistant_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the Wisdom assistant.</p>"""
    assistant_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Wisdom assistant.</p>"""
    association_type: "capo_wisdom.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association_data: "capo_wisdom.types.assistant_association_output_data.AssistantAssociationOutputData"
    """<p>The association data.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationSummary) -> dict:
    out: dict = {}
    out["assistantAssociationId"] = value["assistant_association_id"]
    out["assistantAssociationArn"] = value["assistant_association_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["associationType"] = value["association_type"]
    import capo_wisdom.types.assistant_association_output_data

    out["associationData"] = (
        capo_wisdom.types.assistant_association_output_data.serialize_json(
            value["association_data"]
        )
    )
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
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
        import capo_wisdom.types.assistant_association_output_data

        out["association_data"] = (
            capo_wisdom.types.assistant_association_output_data.deserialize_json(
                data["associationData"]
            )
        )
    else:
        raise DeserializationError(
            "AssistantAssociationSummary.association_data required"
        )
    if "tags" in data:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out
