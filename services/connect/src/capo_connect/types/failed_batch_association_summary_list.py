"""Generated from Smithy shape ``com.amazonaws.connect#FailedBatchAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.failed_batch_association_summary

FailedBatchAssociationSummaryList: TypeAlias = list[
    "capo_connect.types.failed_batch_association_summary.FailedBatchAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedBatchAssociationSummaryList) -> list:
    import capo_connect.types.failed_batch_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.failed_batch_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedBatchAssociationSummaryList:
    import capo_connect.types.failed_batch_association_summary

    out: FailedBatchAssociationSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.failed_batch_association_summary.deserialize_json(item)
        )
    return out
