"""Generated from Smithy shape ``com.amazonaws.mediatailor#RecurringRetrieval``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.traffic_shaping_retrieval_window
    import aws_sdk_mediatailor.types.traffic_shaping_tps_configuration
    import aws_sdk_mediatailor.types.traffic_shaping_type


class RecurringRetrieval(TypedDict):
    dynamic_variables: NotRequired[
        "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
    ]
    """<p>The dynamic variables to use for substitution during prefetch requests to the ADS.</p>"""
    delay_after_avail_end_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail. If not set, the default is 0 (no delay).</p>"""
    traffic_shaping_type: NotRequired[
        "aws_sdk_mediatailor.types.traffic_shaping_type.TrafficShapingType"
    ]
    """<p>Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.</p>"""
    traffic_shaping_retrieval_window: NotRequired[
        "aws_sdk_mediatailor.types.traffic_shaping_retrieval_window.TrafficShapingRetrievalWindow"
    ]
    """<p>The configuration that tells Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.</p>"""
    traffic_shaping_tps_configuration: NotRequired[
        "aws_sdk_mediatailor.types.traffic_shaping_tps_configuration.TrafficShapingTpsConfiguration"
    ]
    """<p>The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringRetrieval) -> dict:
    out: dict = {}
    if "dynamic_variables" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["DynamicVariables"] = (
            aws_sdk_mediatailor.types.__map_of__string.serialize_json(
                value["dynamic_variables"]
            )
        )
    if "delay_after_avail_end_seconds" in value:
        out["DelayAfterAvailEndSeconds"] = value["delay_after_avail_end_seconds"]
    if "traffic_shaping_type" in value:
        import aws_sdk_mediatailor.types.traffic_shaping_type

        out["TrafficShapingType"] = (
            aws_sdk_mediatailor.types.traffic_shaping_type.serialize_json(
                value["traffic_shaping_type"]
            )
        )
    if "traffic_shaping_retrieval_window" in value:
        import aws_sdk_mediatailor.types.traffic_shaping_retrieval_window

        out["TrafficShapingRetrievalWindow"] = (
            aws_sdk_mediatailor.types.traffic_shaping_retrieval_window.serialize_json(
                value["traffic_shaping_retrieval_window"]
            )
        )
    if "traffic_shaping_tps_configuration" in value:
        import aws_sdk_mediatailor.types.traffic_shaping_tps_configuration

        out["TrafficShapingTpsConfiguration"] = (
            aws_sdk_mediatailor.types.traffic_shaping_tps_configuration.serialize_json(
                value["traffic_shaping_tps_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecurringRetrieval:
    out: RecurringRetrieval = {}  # type: ignore[typeddict-item]
    if "DynamicVariables" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["dynamic_variables"] = (
            aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
                data["DynamicVariables"]
            )
        )
    if "DelayAfterAvailEndSeconds" in data:
        out["delay_after_avail_end_seconds"] = data["DelayAfterAvailEndSeconds"]
    if "TrafficShapingType" in data:
        import aws_sdk_mediatailor.types.traffic_shaping_type

        out["traffic_shaping_type"] = (
            aws_sdk_mediatailor.types.traffic_shaping_type.deserialize_json(
                data["TrafficShapingType"]
            )
        )
    if "TrafficShapingRetrievalWindow" in data:
        import aws_sdk_mediatailor.types.traffic_shaping_retrieval_window

        out["traffic_shaping_retrieval_window"] = (
            aws_sdk_mediatailor.types.traffic_shaping_retrieval_window.deserialize_json(
                data["TrafficShapingRetrievalWindow"]
            )
        )
    if "TrafficShapingTpsConfiguration" in data:
        import aws_sdk_mediatailor.types.traffic_shaping_tps_configuration

        out["traffic_shaping_tps_configuration"] = (
            aws_sdk_mediatailor.types.traffic_shaping_tps_configuration.deserialize_json(
                data["TrafficShapingTpsConfiguration"]
            )
        )
    return out
