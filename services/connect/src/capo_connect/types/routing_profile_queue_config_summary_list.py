"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_queue_config_summary

RoutingProfileQueueConfigSummaryList: TypeAlias = list[
    "capo_connect.types.routing_profile_queue_config_summary.RoutingProfileQueueConfigSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfigSummaryList) -> list:
    import capo_connect.types.routing_profile_queue_config_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.routing_profile_queue_config_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingProfileQueueConfigSummaryList:
    import capo_connect.types.routing_profile_queue_config_summary

    out: RoutingProfileQueueConfigSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.routing_profile_queue_config_summary.deserialize_json(
                item
            )
        )
    return out
