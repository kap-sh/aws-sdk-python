"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_summary

AccessorSummaryList: TypeAlias = list[
    "aws_sdk_managedblockchain.types.accessor_summary.AccessorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessorSummaryList) -> list:
    import aws_sdk_managedblockchain.types.accessor_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_managedblockchain.types.accessor_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessorSummaryList:
    import aws_sdk_managedblockchain.types.accessor_summary

    out: AccessorSummaryList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain.types.accessor_summary.deserialize_json(item)
        )
    return out
