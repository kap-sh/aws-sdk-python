"""Generated from Smithy shape ``com.amazonaws.voiceid#EnrollmentJobFraudDetectionConfigWatchlistIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.watchlist_id

EnrollmentJobFraudDetectionConfigWatchlistIds: TypeAlias = list[
    "capo_voice_id.types.watchlist_id.WatchlistId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: EnrollmentJobFraudDetectionConfigWatchlistIds,
) -> list:
    return list(value)


def deserialize_aws_json_1_0(
    data: list,
) -> EnrollmentJobFraudDetectionConfigWatchlistIds:
    return list(data)
