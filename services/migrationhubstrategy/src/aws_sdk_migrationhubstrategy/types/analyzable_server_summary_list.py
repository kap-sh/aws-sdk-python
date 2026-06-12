"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalyzableServerSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.analyzable_server_summary

AnalyzableServerSummaryList: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.analyzable_server_summary.AnalyzableServerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzableServerSummaryList) -> list:
    import aws_sdk_migrationhubstrategy.types.analyzable_server_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.analyzable_server_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyzableServerSummaryList:
    import aws_sdk_migrationhubstrategy.types.analyzable_server_summary

    out: AnalyzableServerSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.analyzable_server_summary.deserialize_json(
                item
            )
        )
    return out
