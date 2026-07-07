"""Generated from Smithy shape ``com.amazonaws.connect#ListRoutingProfileManualAssignmentQueuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list
    import aws_sdk_connect.types.timestamp


class ListRoutingProfileManualAssignmentQueuesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    routing_profile_manual_assignment_queue_config_summary_list: NotRequired[
        "aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list.RoutingProfileManualAssignmentQueueConfigSummaryList"
    ]
    """<p>Information about the manual assignment queues associated with the routing profile.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingProfileManualAssignmentQueuesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "routing_profile_manual_assignment_queue_config_summary_list" in value:
        import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list

        out["RoutingProfileManualAssignmentQueueConfigSummaryList"] = (
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list.serialize_json(
                value["routing_profile_manual_assignment_queue_config_summary_list"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListRoutingProfileManualAssignmentQueuesResponse:
    out: ListRoutingProfileManualAssignmentQueuesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RoutingProfileManualAssignmentQueueConfigSummaryList" in data:
        import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list

        out["routing_profile_manual_assignment_queue_config_summary_list"] = (
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config_summary_list.deserialize_json(
                data["RoutingProfileManualAssignmentQueueConfigSummaryList"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
