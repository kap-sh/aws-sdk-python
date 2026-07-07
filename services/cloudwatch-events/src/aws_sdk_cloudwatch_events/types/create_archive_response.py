"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.archive_arn
    import aws_sdk_cloudwatch_events.types.archive_state
    import aws_sdk_cloudwatch_events.types.archive_state_reason
    import aws_sdk_cloudwatch_events.types.timestamp


class CreateArchiveResponse(TypedDict, closed=True):
    archive_arn: NotRequired["aws_sdk_cloudwatch_events.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive that was created.</p>"""
    state: NotRequired["aws_sdk_cloudwatch_events.types.archive_state.ArchiveState"]
    """<p>The state of the archive that was created.</p>"""
    state_reason: NotRequired[
        "aws_sdk_cloudwatch_events.types.archive_state_reason.ArchiveStateReason"
    ]
    """<p>The reason that the archive is in the state.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>The time at which the archive was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateArchiveResponse) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    if "state" in value:
        import aws_sdk_cloudwatch_events.types.archive_state

        out["State"] = (
            aws_sdk_cloudwatch_events.types.archive_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "creation_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateArchiveResponse:
    out: CreateArchiveResponse = {}  # type: ignore[typeddict-item]
    if "ArchiveArn" in data:
        out["archive_arn"] = data["ArchiveArn"]
    if "State" in data:
        import aws_sdk_cloudwatch_events.types.archive_state

        out["state"] = (
            aws_sdk_cloudwatch_events.types.archive_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "CreationTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
