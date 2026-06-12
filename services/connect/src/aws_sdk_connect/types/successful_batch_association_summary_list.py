"""Generated from Smithy shape ``com.amazonaws.connect#SuccessfulBatchAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.successful_batch_association_summary

SuccessfulBatchAssociationSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.successful_batch_association_summary.SuccessfulBatchAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulBatchAssociationSummaryList) -> list:
    import aws_sdk_connect.types.successful_batch_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.successful_batch_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuccessfulBatchAssociationSummaryList:
    import aws_sdk_connect.types.successful_batch_association_summary

    out: SuccessfulBatchAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.successful_batch_association_summary.deserialize_json(
                item
            )
        )
    return out
