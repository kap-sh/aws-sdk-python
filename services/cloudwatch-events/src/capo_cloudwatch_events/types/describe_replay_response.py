"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeReplayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.arn
    import capo_cloudwatch_events.types.replay_arn
    import capo_cloudwatch_events.types.replay_description
    import capo_cloudwatch_events.types.replay_destination
    import capo_cloudwatch_events.types.replay_name
    import capo_cloudwatch_events.types.replay_state
    import capo_cloudwatch_events.types.replay_state_reason
    import capo_cloudwatch_events.types.timestamp


class DescribeReplayResponse(TypedDict, closed=True):
    replay_name: NotRequired["capo_cloudwatch_events.types.replay_name.ReplayName"]
    """<p>The name of the replay.</p>"""
    replay_arn: NotRequired["capo_cloudwatch_events.types.replay_arn.ReplayArn"]
    """<p>The ARN of the replay.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.replay_description.ReplayDescription"
    ]
    """<p>The description of the replay.</p>"""
    state: NotRequired["capo_cloudwatch_events.types.replay_state.ReplayState"]
    """<p>The current state of the replay.</p>"""
    state_reason: NotRequired[
        "capo_cloudwatch_events.types.replay_state_reason.ReplayStateReason"
    ]
    """<p>The reason that the replay is in the current state.</p>"""
    event_source_arn: NotRequired["capo_cloudwatch_events.types.arn.Arn"]
    """<p>The ARN of the archive events were replayed from.</p>"""
    destination: NotRequired[
        "capo_cloudwatch_events.types.replay_destination.ReplayDestination"
    ]
    """<p>A <code>ReplayDestination</code> object that contains details about the replay.</p>"""
    event_start_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>The time stamp of the first event that was last replayed from the archive.</p>"""
    event_end_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>The time stamp for the last event that was replayed from the archive.</p>"""
    event_last_replayed_time: NotRequired[
        "capo_cloudwatch_events.types.timestamp.Timestamp"
    ]
    """<p>The time that the event was last replayed.</p>"""
    replay_start_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the replay started.</p>"""
    replay_end_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the replay stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplayResponse) -> dict:
    out: dict = {}
    if "replay_name" in value:
        out["ReplayName"] = value["replay_name"]
    if "replay_arn" in value:
        out["ReplayArn"] = value["replay_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_cloudwatch_events.types.replay_state

        out["State"] = capo_cloudwatch_events.types.replay_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "destination" in value:
        import capo_cloudwatch_events.types.replay_destination

        out["Destination"] = (
            capo_cloudwatch_events.types.replay_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "event_start_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["EventStartTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["event_start_time"]
            )
        )
    if "event_end_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["EventEndTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["event_end_time"]
            )
        )
    if "event_last_replayed_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["EventLastReplayedTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["event_last_replayed_time"]
            )
        )
    if "replay_start_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["ReplayStartTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["replay_start_time"]
            )
        )
    if "replay_end_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["ReplayEndTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["replay_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplayResponse:
    out: DescribeReplayResponse = {}  # type: ignore[typeddict-item]
    if "ReplayName" in data:
        out["replay_name"] = data["ReplayName"]
    if "ReplayArn" in data:
        out["replay_arn"] = data["ReplayArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import capo_cloudwatch_events.types.replay_state

        out["state"] = (
            capo_cloudwatch_events.types.replay_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "Destination" in data:
        import capo_cloudwatch_events.types.replay_destination

        out["destination"] = (
            capo_cloudwatch_events.types.replay_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    if "EventStartTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["event_start_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["EventStartTime"]
            )
        )
    if "EventEndTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["event_end_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["EventEndTime"]
            )
        )
    if "EventLastReplayedTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["event_last_replayed_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["EventLastReplayedTime"]
            )
        )
    if "ReplayStartTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["replay_start_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["ReplayStartTime"]
            )
        )
    if "ReplayEndTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["replay_end_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["ReplayEndTime"]
            )
        )
    return out
