"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationshipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.composition_relationship_summary

CompositionRelationshipSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.composition_relationship_summary.CompositionRelationshipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationshipSummaries) -> list:
    import aws_sdk_iotsitewise.types.composition_relationship_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.composition_relationship_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CompositionRelationshipSummaries:
    import aws_sdk_iotsitewise.types.composition_relationship_summary

    out: CompositionRelationshipSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.composition_relationship_summary.deserialize_json(
                item
            )
        )
    return out
