"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutLogEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.rejected_entity_info
    import capo_cloudwatch_logs.types.rejected_log_events_info
    import capo_cloudwatch_logs.types.sequence_token


class PutLogEventsResponse(TypedDict, closed=True):
    next_sequence_token: NotRequired[
        "capo_cloudwatch_logs.types.sequence_token.SequenceToken"
    ]
    """<p>The next sequence token.</p> <important> <p>This field has been deprecated.</p> <p>The sequence token is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are always accepted even if the sequence token is not valid. You can use parallel <code>PutLogEvents</code> actions on the same log stream and you do not need to wait for the response of a previous <code>PutLogEvents</code> action to obtain the <code>nextSequenceToken</code> value.</p> </important>"""
    rejected_log_events_info: NotRequired[
        "capo_cloudwatch_logs.types.rejected_log_events_info.RejectedLogEventsInfo"
    ]
    """<p>The rejected events.</p>"""
    rejected_entity_info: NotRequired[
        "capo_cloudwatch_logs.types.rejected_entity_info.RejectedEntityInfo"
    ]
    """<p>Information about why the entity is rejected when calling <code>PutLogEvents</code>. Only returned when the entity is rejected.</p> <note> <p>When the entity is rejected, the events may still be accepted.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLogEventsResponse) -> dict:
    out: dict = {}
    if "next_sequence_token" in value:
        out["nextSequenceToken"] = value["next_sequence_token"]
    if "rejected_log_events_info" in value:
        import capo_cloudwatch_logs.types.rejected_log_events_info

        out["rejectedLogEventsInfo"] = (
            capo_cloudwatch_logs.types.rejected_log_events_info.serialize_aws_json_1_1(
                value["rejected_log_events_info"]
            )
        )
    if "rejected_entity_info" in value:
        import capo_cloudwatch_logs.types.rejected_entity_info

        out["rejectedEntityInfo"] = (
            capo_cloudwatch_logs.types.rejected_entity_info.serialize_aws_json_1_1(
                value["rejected_entity_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLogEventsResponse:
    out: PutLogEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextSequenceToken") is not None:
        out["next_sequence_token"] = data["nextSequenceToken"]
    if data.get("rejectedLogEventsInfo") is not None:
        import capo_cloudwatch_logs.types.rejected_log_events_info

        out["rejected_log_events_info"] = (
            capo_cloudwatch_logs.types.rejected_log_events_info.deserialize_aws_json_1_1(
                data["rejectedLogEventsInfo"]
            )
        )
    if data.get("rejectedEntityInfo") is not None:
        import capo_cloudwatch_logs.types.rejected_entity_info

        out["rejected_entity_info"] = (
            capo_cloudwatch_logs.types.rejected_entity_info.deserialize_aws_json_1_1(
                data["rejectedEntityInfo"]
            )
        )
    return out
