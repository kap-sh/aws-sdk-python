"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreatePrefetchScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.prefetch_consumption
    import aws_sdk_mediatailor.types.prefetch_retrieval
    import aws_sdk_mediatailor.types.prefetch_schedule_type
    import aws_sdk_mediatailor.types.recurring_prefetch_configuration


class CreatePrefetchScheduleRequest(TypedDict):
    consumption: NotRequired[
        "aws_sdk_mediatailor.types.prefetch_consumption.PrefetchConsumption"
    ]
    """<p>The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the <i>consumption window</i>. Prefetch schedules automatically expire no earlier than seven days after the end time.</p>"""
    name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name to assign to the schedule request.</p>"""
    playback_configuration_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name to assign to the playback configuration.</p>"""
    retrieval: NotRequired[
        "aws_sdk_mediatailor.types.prefetch_retrieval.PrefetchRetrieval"
    ]
    """<p>The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.</p>"""
    recurring_prefetch_configuration: NotRequired[
        "aws_sdk_mediatailor.types.recurring_prefetch_configuration.RecurringPrefetchConfiguration"
    ]
    """<p>The configuration that defines how and when MediaTailor performs ad prefetching in a live event.</p>"""
    schedule_type: NotRequired[
        "aws_sdk_mediatailor.types.prefetch_schedule_type.PrefetchScheduleType"
    ]
    """<p>The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.</p> <p>For more information about the prefetch types and when you might use each, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\">Prefetching ads in Elemental MediaTailor.</a> </p>"""
    stream_id: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If <code>StreamId</code> is specified, MediaTailor returns all of the prefetch schedules with an exact match on <code>StreamId</code>. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of <code>StreamId</code>.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrefetchScheduleRequest) -> dict:
    out: dict = {}
    if "consumption" in value:
        import aws_sdk_mediatailor.types.prefetch_consumption

        out["Consumption"] = (
            aws_sdk_mediatailor.types.prefetch_consumption.serialize_json(
                value["consumption"]
            )
        )
    if "retrieval" in value:
        import aws_sdk_mediatailor.types.prefetch_retrieval

        out["Retrieval"] = aws_sdk_mediatailor.types.prefetch_retrieval.serialize_json(
            value["retrieval"]
        )
    if "recurring_prefetch_configuration" in value:
        import aws_sdk_mediatailor.types.recurring_prefetch_configuration

        out["RecurringPrefetchConfiguration"] = (
            aws_sdk_mediatailor.types.recurring_prefetch_configuration.serialize_json(
                value["recurring_prefetch_configuration"]
            )
        )
    if "schedule_type" in value:
        import aws_sdk_mediatailor.types.prefetch_schedule_type

        out["ScheduleType"] = (
            aws_sdk_mediatailor.types.prefetch_schedule_type.serialize_json(
                value["schedule_type"]
            )
        )
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePrefetchScheduleRequest:
    out: CreatePrefetchScheduleRequest = {}  # type: ignore[typeddict-item]
    if "Consumption" in data:
        import aws_sdk_mediatailor.types.prefetch_consumption

        out["consumption"] = (
            aws_sdk_mediatailor.types.prefetch_consumption.deserialize_json(
                data["Consumption"]
            )
        )
    if "Retrieval" in data:
        import aws_sdk_mediatailor.types.prefetch_retrieval

        out["retrieval"] = (
            aws_sdk_mediatailor.types.prefetch_retrieval.deserialize_json(
                data["Retrieval"]
            )
        )
    if "RecurringPrefetchConfiguration" in data:
        import aws_sdk_mediatailor.types.recurring_prefetch_configuration

        out["recurring_prefetch_configuration"] = (
            aws_sdk_mediatailor.types.recurring_prefetch_configuration.deserialize_json(
                data["RecurringPrefetchConfiguration"]
            )
        )
    if "ScheduleType" in data:
        import aws_sdk_mediatailor.types.prefetch_schedule_type

        out["schedule_type"] = (
            aws_sdk_mediatailor.types.prefetch_schedule_type.deserialize_json(
                data["ScheduleType"]
            )
        )
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
