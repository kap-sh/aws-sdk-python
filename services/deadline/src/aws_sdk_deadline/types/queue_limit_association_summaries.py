"""Generated from Smithy shape ``com.amazonaws.deadline#QueueLimitAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_limit_association_summary

QueueLimitAssociationSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.queue_limit_association_summary.QueueLimitAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueLimitAssociationSummaries) -> list:
    import aws_sdk_deadline.types.queue_limit_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.queue_limit_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QueueLimitAssociationSummaries:
    import aws_sdk_deadline.types.queue_limit_association_summary

    out: QueueLimitAssociationSummaries = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.queue_limit_association_summary.deserialize_json(
                item
            )
        )
    return out
