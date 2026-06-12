"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileManualAssignmentQueueConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary

RoutingProfileManualAssignmentQueueConfigSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary.RoutingProfileManualAssignmentQueueConfigSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileManualAssignmentQueueConfigSummaryList) -> list:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RoutingProfileManualAssignmentQueueConfigSummaryList:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary

    out: RoutingProfileManualAssignmentQueueConfigSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary.deserialize_json(
                item
            )
        )
    return out
