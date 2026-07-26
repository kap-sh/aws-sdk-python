"""Generated from Smithy shape ``com.amazonaws.migrationhub#ProgressUpdateStreamSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.progress_update_stream_summary

ProgressUpdateStreamSummaryList: TypeAlias = list[
    "capo_migration_hub.types.progress_update_stream_summary.ProgressUpdateStreamSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProgressUpdateStreamSummaryList) -> list:
    import capo_migration_hub.types.progress_update_stream_summary

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.progress_update_stream_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProgressUpdateStreamSummaryList:
    import capo_migration_hub.types.progress_update_stream_summary

    out: ProgressUpdateStreamSummaryList = []
    for item in data:
        out.append(
            capo_migration_hub.types.progress_update_stream_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
