"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.backfill_mode
    import aws_sdk_gamelift.types.boolean_model
    import aws_sdk_gamelift.types.custom_event_data
    import aws_sdk_gamelift.types.flex_match_mode
    import aws_sdk_gamelift.types.game_property_list
    import aws_sdk_gamelift.types.game_session_data
    import aws_sdk_gamelift.types.matchmaking_acceptance_timeout_integer
    import aws_sdk_gamelift.types.matchmaking_id_string_model
    import aws_sdk_gamelift.types.matchmaking_request_timeout_integer
    import aws_sdk_gamelift.types.matchmaking_rule_set_name
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.queue_arns_list
    import aws_sdk_gamelift.types.sns_arn_string_model
    import aws_sdk_gamelift.types.tag_list
    import aws_sdk_gamelift.types.whole_number


class CreateMatchmakingConfigurationInput(TypedDict):
    name: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.</p>"""
    description: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A human-readable description of the matchmaking configuration. </p>"""
    game_session_queue_arns: NotRequired[
        "aws_sdk_gamelift.types.queue_arns_list.QueueArnsList"
    ]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::gamesessionqueue/<queue name></code>. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If <code>FlexMatchMode</code> is set to <code>STANDALONE</code>, do not set this parameter. </p>"""
    request_timeout_seconds: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_request_timeout_integer.MatchmakingRequestTimeoutInteger"
    ]
    """<p>The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.</p>"""
    acceptance_timeout_seconds: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_acceptance_timeout_integer.MatchmakingAcceptanceTimeoutInteger"
    ]
    """<p>The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required. </p>"""
    acceptance_required: NotRequired[
        "aws_sdk_gamelift.types.boolean_model.BooleanModel"
    ]
    """<p>A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to <code>TRUE</code>. With this option enabled, matchmaking tickets use the status <code>REQUIRES_ACCEPTANCE</code> to indicate when a completed potential match is waiting for player acceptance. </p>"""
    rule_set_name: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
    ]
    """<p>A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.</p>"""
    notification_target: NotRequired[
        "aws_sdk_gamelift.types.sns_arn_string_model.SnsArnStringModel"
    ]
    r"""<p>An SNS topic ARN that is set up to receive matchmaking notifications. See <a href=\"https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html\"> Setting up notifications for matchmaking</a> for more information.</p>"""
    additional_player_count: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    custom_event_data: NotRequired[
        "aws_sdk_gamelift.types.custom_event_data.CustomEventData"
    ]
    """<p>Information to be added to all events related to this matchmaking configuration. </p>"""
    game_properties: NotRequired[
        "aws_sdk_gamelift.types.game_property_list.GamePropertyList"
    ]
    r"""<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{\"Key\": \"difficulty\", \"Value\": \"novice\"}</code>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p> <note> <ul> <li> <p>Avoid using periods (\".\") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    game_session_data: NotRequired[
        "aws_sdk_gamelift.types.game_session_data.GameSessionData"
    ]
    r"""<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession\">Start a game session</a>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    backfill_mode: NotRequired["aws_sdk_gamelift.types.backfill_mode.BackfillMode"]
    r"""<p>The method used to backfill game sessions that are created with this matchmaking configuration. Specify <code>MANUAL</code> when your game manages backfill requests manually or does not use the match backfill feature. Specify <code>AUTOMATIC</code> to have Amazon GameLift Servers create a backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in <a href=\"https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html\"> Backfill Existing Games with FlexMatch</a>. Automatic backfill is not available when <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    flex_match_mode: NotRequired["aws_sdk_gamelift.types.flex_match_mode.FlexMatchMode"]
    r"""<p>Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. </p> <ul> <li> <p> <b>STANDALONE</b> - FlexMatch forms matches and returns match information, including players and team assignments, in a <a href=\"https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded\"> MatchmakingSucceeded</a> event.</p> </li> <li> <p> <b>WITH_QUEUE</b> - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match. </p> </li> </ul>"""
    tags: NotRequired["aws_sdk_gamelift.types.tag_list.TagList"]
    r"""<p>A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management and cost allocation. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "game_session_queue_arns" in value:
        import aws_sdk_gamelift.types.queue_arns_list

        out["GameSessionQueueArns"] = (
            aws_sdk_gamelift.types.queue_arns_list.serialize_aws_json_1_1(
                value["game_session_queue_arns"]
            )
        )
    if "request_timeout_seconds" in value:
        out["RequestTimeoutSeconds"] = value["request_timeout_seconds"]
    if "acceptance_timeout_seconds" in value:
        out["AcceptanceTimeoutSeconds"] = value["acceptance_timeout_seconds"]
    if "acceptance_required" in value:
        out["AcceptanceRequired"] = value["acceptance_required"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "notification_target" in value:
        out["NotificationTarget"] = value["notification_target"]
    if "additional_player_count" in value:
        out["AdditionalPlayerCount"] = value["additional_player_count"]
    if "custom_event_data" in value:
        out["CustomEventData"] = value["custom_event_data"]
    if "game_properties" in value:
        import aws_sdk_gamelift.types.game_property_list

        out["GameProperties"] = (
            aws_sdk_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "backfill_mode" in value:
        import aws_sdk_gamelift.types.backfill_mode

        out["BackfillMode"] = (
            aws_sdk_gamelift.types.backfill_mode.serialize_aws_json_1_1(
                value["backfill_mode"]
            )
        )
    if "flex_match_mode" in value:
        import aws_sdk_gamelift.types.flex_match_mode

        out["FlexMatchMode"] = (
            aws_sdk_gamelift.types.flex_match_mode.serialize_aws_json_1_1(
                value["flex_match_mode"]
            )
        )
    if "tags" in value:
        import aws_sdk_gamelift.types.tag_list

        out["Tags"] = aws_sdk_gamelift.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingConfigurationInput:
    out: CreateMatchmakingConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "GameSessionQueueArns" in data:
        import aws_sdk_gamelift.types.queue_arns_list

        out["game_session_queue_arns"] = (
            aws_sdk_gamelift.types.queue_arns_list.deserialize_aws_json_1_1(
                data["GameSessionQueueArns"]
            )
        )
    if "RequestTimeoutSeconds" in data:
        out["request_timeout_seconds"] = data["RequestTimeoutSeconds"]
    if "AcceptanceTimeoutSeconds" in data:
        out["acceptance_timeout_seconds"] = data["AcceptanceTimeoutSeconds"]
    if "AcceptanceRequired" in data:
        out["acceptance_required"] = data["AcceptanceRequired"]
    if "RuleSetName" in data:
        out["rule_set_name"] = data["RuleSetName"]
    if "NotificationTarget" in data:
        out["notification_target"] = data["NotificationTarget"]
    if "AdditionalPlayerCount" in data:
        out["additional_player_count"] = data["AdditionalPlayerCount"]
    if "CustomEventData" in data:
        out["custom_event_data"] = data["CustomEventData"]
    if "GameProperties" in data:
        import aws_sdk_gamelift.types.game_property_list

        out["game_properties"] = (
            aws_sdk_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    if "GameSessionData" in data:
        out["game_session_data"] = data["GameSessionData"]
    if "BackfillMode" in data:
        import aws_sdk_gamelift.types.backfill_mode

        out["backfill_mode"] = (
            aws_sdk_gamelift.types.backfill_mode.deserialize_aws_json_1_1(
                data["BackfillMode"]
            )
        )
    if "FlexMatchMode" in data:
        import aws_sdk_gamelift.types.flex_match_mode

        out["flex_match_mode"] = (
            aws_sdk_gamelift.types.flex_match_mode.deserialize_aws_json_1_1(
                data["FlexMatchMode"]
            )
        )
    if "Tags" in data:
        import aws_sdk_gamelift.types.tag_list

        out["tags"] = aws_sdk_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
