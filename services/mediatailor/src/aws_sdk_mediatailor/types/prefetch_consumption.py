"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchConsumption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria
    import aws_sdk_mediatailor.types.__timestamp_unix


class PrefetchConsumption(TypedDict, closed=True):
    avail_matching_criteria: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.__listOfAvailMatchingCriteria"
    ]
    """<p>If you only want MediaTailor to insert prefetched ads into avails (ad breaks) that match specific dynamic variables, such as <code>scte.event_id</code>, set the avail matching criteria.</p>"""
    end_time: "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The time when MediaTailor no longer considers the prefetched ads for use in an ad break. MediaTailor automatically deletes prefetch schedules no less than seven days after the end time. If you'd like to manually delete the prefetch schedule, you can call <code>DeletePrefetchSchedule</code>.</p>"""
    start_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The time when prefetched ads are considered for use in an ad break. If you don't specify <code>StartTime</code>, the prefetched ads are available after MediaTailor retrieves them from the ad decision server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrefetchConsumption) -> dict:
    out: dict = {}
    if "avail_matching_criteria" in value:
        import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria

        out["AvailMatchingCriteria"] = (
            aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.serialize_json(
                value["avail_matching_criteria"]
            )
        )
    import aws_sdk_mediatailor.types.__timestamp_unix

    out["EndTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
        value["end_time"]
    )
    if "start_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["StartTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> PrefetchConsumption:
    out: PrefetchConsumption = {}  # type: ignore[typeddict-item]
    if "AvailMatchingCriteria" in data:
        import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria

        out["avail_matching_criteria"] = (
            aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.deserialize_json(
                data["AvailMatchingCriteria"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["end_time"] = aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
            data["EndTime"]
        )
    else:
        raise DeserializationError("PrefetchConsumption.end_time required")
    if "StartTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["start_time"] = aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
            data["StartTime"]
        )
    return out
