"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameSessionQueueInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.filter_configuration
    import aws_sdk_gamelift.types.game_session_queue_destination_list
    import aws_sdk_gamelift.types.game_session_queue_name_or_arn
    import aws_sdk_gamelift.types.player_latency_policy_list
    import aws_sdk_gamelift.types.priority_configuration
    import aws_sdk_gamelift.types.queue_custom_event_data
    import aws_sdk_gamelift.types.queue_sns_arn_string_model
    import aws_sdk_gamelift.types.whole_number


class UpdateGameSessionQueueInput(TypedDict):
    name: NotRequired[
        "aws_sdk_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
    ]
    """<p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value. </p>"""
    timeout_in_seconds: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a <code>TIMED_OUT</code> status.</p> <note> <p>The minimum value is 10 and the maximum value is 600.</p> </note>"""
    player_latency_policies: NotRequired[
        "aws_sdk_gamelift.types.player_latency_policy_list.PlayerLatencyPolicyList"
    ]
    """<p>A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value. When updating policies, provide a complete collection of policies.</p>"""
    destinations: NotRequired[
        "aws_sdk_gamelift.types.game_session_queue_destination_list.GameSessionQueueDestinationList"
    ]
    """<p>A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference. When updating this list, provide a complete list of destinations.</p>"""
    filter_configuration: NotRequired[
        "aws_sdk_gamelift.types.filter_configuration.FilterConfiguration"
    ]
    """<p>A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as <code>us-west-2</code>. If this parameter is not set, game sessions can be placed in any queue location. To remove an existing filter configuration, pass in an empty set.</p>"""
    priority_configuration: NotRequired[
        "aws_sdk_gamelift.types.priority_configuration.PriorityConfiguration"
    ]
    """<p>Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. To remove an existing priority configuration, pass in an empty set.</p>"""
    custom_event_data: NotRequired[
        "aws_sdk_gamelift.types.queue_custom_event_data.QueueCustomEventData"
    ]
    """<p>Information to be added to all events that are related to this game session queue.</p>"""
    notification_target: NotRequired[
        "aws_sdk_gamelift.types.queue_sns_arn_string_model.QueueSnsArnStringModel"
    ]
    r"""<p>An SNS topic ARN that is set up to receive game session placement notifications. See <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html\"> Setting up notifications for game session placement</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameSessionQueueInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    if "player_latency_policies" in value:
        import aws_sdk_gamelift.types.player_latency_policy_list

        out["PlayerLatencyPolicies"] = (
            aws_sdk_gamelift.types.player_latency_policy_list.serialize_aws_json_1_1(
                value["player_latency_policies"]
            )
        )
    if "destinations" in value:
        import aws_sdk_gamelift.types.game_session_queue_destination_list

        out["Destinations"] = (
            aws_sdk_gamelift.types.game_session_queue_destination_list.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "filter_configuration" in value:
        import aws_sdk_gamelift.types.filter_configuration

        out["FilterConfiguration"] = (
            aws_sdk_gamelift.types.filter_configuration.serialize_aws_json_1_1(
                value["filter_configuration"]
            )
        )
    if "priority_configuration" in value:
        import aws_sdk_gamelift.types.priority_configuration

        out["PriorityConfiguration"] = (
            aws_sdk_gamelift.types.priority_configuration.serialize_aws_json_1_1(
                value["priority_configuration"]
            )
        )
    if "custom_event_data" in value:
        out["CustomEventData"] = value["custom_event_data"]
    if "notification_target" in value:
        out["NotificationTarget"] = value["notification_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameSessionQueueInput:
    out: UpdateGameSessionQueueInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TimeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    if "PlayerLatencyPolicies" in data:
        import aws_sdk_gamelift.types.player_latency_policy_list

        out["player_latency_policies"] = (
            aws_sdk_gamelift.types.player_latency_policy_list.deserialize_aws_json_1_1(
                data["PlayerLatencyPolicies"]
            )
        )
    if "Destinations" in data:
        import aws_sdk_gamelift.types.game_session_queue_destination_list

        out["destinations"] = (
            aws_sdk_gamelift.types.game_session_queue_destination_list.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if "FilterConfiguration" in data:
        import aws_sdk_gamelift.types.filter_configuration

        out["filter_configuration"] = (
            aws_sdk_gamelift.types.filter_configuration.deserialize_aws_json_1_1(
                data["FilterConfiguration"]
            )
        )
    if "PriorityConfiguration" in data:
        import aws_sdk_gamelift.types.priority_configuration

        out["priority_configuration"] = (
            aws_sdk_gamelift.types.priority_configuration.deserialize_aws_json_1_1(
                data["PriorityConfiguration"]
            )
        )
    if "CustomEventData" in data:
        out["custom_event_data"] = data["CustomEventData"]
    if "NotificationTarget" in data:
        out["notification_target"] = data["NotificationTarget"]
    return out
