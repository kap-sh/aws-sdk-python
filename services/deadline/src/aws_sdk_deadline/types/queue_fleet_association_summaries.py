"""Generated from Smithy shape ``com.amazonaws.deadline#QueueFleetAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_fleet_association_summary

QueueFleetAssociationSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.queue_fleet_association_summary.QueueFleetAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueFleetAssociationSummaries) -> list:
    import aws_sdk_deadline.types.queue_fleet_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.queue_fleet_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QueueFleetAssociationSummaries:
    import aws_sdk_deadline.types.queue_fleet_association_summary

    out: QueueFleetAssociationSummaries = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.queue_fleet_association_summary.deserialize_json(
                item
            )
        )
    return out
