"""Generated from Smithy shape ``com.amazonaws.voiceid#WatchlistSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.watchlist_summary

WatchlistSummaries: TypeAlias = list[
    "aws_sdk_voice_id.types.watchlist_summary.WatchlistSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WatchlistSummaries) -> list:
    import aws_sdk_voice_id.types.watchlist_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_voice_id.types.watchlist_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WatchlistSummaries:
    import aws_sdk_voice_id.types.watchlist_summary

    out: WatchlistSummaries = []
    for item in data:
        out.append(
            aws_sdk_voice_id.types.watchlist_summary.deserialize_aws_json_1_0(item)
        )
    return out
