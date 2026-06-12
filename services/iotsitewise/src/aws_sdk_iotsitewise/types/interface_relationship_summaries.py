"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceRelationshipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.interface_relationship_summary

InterfaceRelationshipSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.interface_relationship_summary.InterfaceRelationshipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceRelationshipSummaries) -> list:
    import aws_sdk_iotsitewise.types.interface_relationship_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.interface_relationship_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InterfaceRelationshipSummaries:
    import aws_sdk_iotsitewise.types.interface_relationship_summary

    out: InterfaceRelationshipSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.interface_relationship_summary.deserialize_json(
                item
            )
        )
    return out
