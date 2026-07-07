"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive_arn
    import aws_sdk_eventbridge.types.archive_description
    import aws_sdk_eventbridge.types.archive_name
    import aws_sdk_eventbridge.types.archive_state
    import aws_sdk_eventbridge.types.archive_state_reason
    import aws_sdk_eventbridge.types.event_bus_arn
    import aws_sdk_eventbridge.types.event_pattern
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.long
    import aws_sdk_eventbridge.types.retention_days
    import aws_sdk_eventbridge.types.timestamp


class DescribeArchiveResponse(TypedDict, closed=True):
    archive_arn: NotRequired["aws_sdk_eventbridge.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive.</p>"""
    archive_name: NotRequired["aws_sdk_eventbridge.types.archive_name.ArchiveName"]
    """<p>The name of the archive.</p>"""
    event_source_arn: NotRequired["aws_sdk_eventbridge.types.event_bus_arn.EventBusArn"]
    """<p>The ARN of the event source associated with the archive.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.archive_description.ArchiveDescription"
    ]
    """<p>The description of the archive.</p>"""
    event_pattern: NotRequired["aws_sdk_eventbridge.types.event_pattern.EventPattern"]
    """<p>The event pattern used to filter events sent to the archive.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.archive_state.ArchiveState"]
    """<p>The state of the archive.</p>"""
    state_reason: NotRequired[
        "aws_sdk_eventbridge.types.archive_state_reason.ArchiveStateReason"
    ]
    """<p>The reason that the archive is in the state.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    r"""<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt this archive, if one has been specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html\">Encrypting archives</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    retention_days: NotRequired[
        "aws_sdk_eventbridge.types.retention_days.RetentionDays"
    ]
    """<p>The number of days to retain events for in the archive.</p>"""
    size_bytes: "aws_sdk_eventbridge.types.long.Long"
    """<p>The size of the archive in bytes.</p>"""
    event_count: "aws_sdk_eventbridge.types.long.Long"
    """<p>The number of events in the archive.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time at which the archive was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeArchiveResponse) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import aws_sdk_eventbridge.types.archive_state

        out["State"] = aws_sdk_eventbridge.types.archive_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    out["SizeBytes"] = value.get("size_bytes", 0)
    out["EventCount"] = value.get("event_count", 0)
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeArchiveResponse:
    out: DescribeArchiveResponse = {}  # type: ignore[typeddict-item]
    if "ArchiveArn" in data:
        out["archive_arn"] = data["ArchiveArn"]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "State" in data:
        import aws_sdk_eventbridge.types.archive_state

        out["state"] = aws_sdk_eventbridge.types.archive_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    if "SizeBytes" in data:
        out["size_bytes"] = data["SizeBytes"]
    else:
        out["size_bytes"] = 0
    if "EventCount" in data:
        out["event_count"] = data["EventCount"]
    else:
        out["event_count"] = 0
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
