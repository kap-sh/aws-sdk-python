"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_arn
    import capo_eventbridge.types.archive_state
    import capo_eventbridge.types.archive_state_reason
    import capo_eventbridge.types.timestamp


class UpdateArchiveResponse(TypedDict, closed=True):
    archive_arn: NotRequired["capo_eventbridge.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive.</p>"""
    state: NotRequired["capo_eventbridge.types.archive_state.ArchiveState"]
    """<p>The state of the archive.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.archive_state_reason.ArchiveStateReason"
    ]
    """<p>The reason that the archive is in the current state.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time at which the archive was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateArchiveResponse) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    if "state" in value:
        import capo_eventbridge.types.archive_state

        out["State"] = capo_eventbridge.types.archive_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateArchiveResponse:
    out: UpdateArchiveResponse = {}  # type: ignore[typeddict-item]
    if "ArchiveArn" in data:
        out["archive_arn"] = data["ArchiveArn"]
    if "State" in data:
        import capo_eventbridge.types.archive_state

        out["state"] = capo_eventbridge.types.archive_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "CreationTime" in data:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
