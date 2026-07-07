"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_event_metadata
    import aws_sdk_codecommit.types.approval_rule_overridden_event_metadata
    import aws_sdk_codecommit.types.approval_state_changed_event_metadata
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.event_date
    import aws_sdk_codecommit.types.pull_request_created_event_metadata
    import aws_sdk_codecommit.types.pull_request_event_type
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata
    import aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata
    import aws_sdk_codecommit.types.pull_request_status_changed_event_metadata


class PullRequestEvent(TypedDict, closed=True):
    pull_request_id: NotRequired[
        "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    ]
    """<p>The system-generated ID of the pull request.</p>"""
    event_date: NotRequired["aws_sdk_codecommit.types.event_date.EventDate"]
    """<p>The day and time of the pull request event, in timestamp format.</p>"""
    pull_request_event_type: NotRequired[
        "aws_sdk_codecommit.types.pull_request_event_type.PullRequestEventType"
    ]
    """<p>The type of the pull request event (for example, a status change event (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED)).</p>"""
    actor_arn: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.</p>"""
    pull_request_created_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.pull_request_created_event_metadata.PullRequestCreatedEventMetadata"
    ]
    """<p>Information about the source and destination branches for the pull request.</p>"""
    pull_request_status_changed_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.pull_request_status_changed_event_metadata.PullRequestStatusChangedEventMetadata"
    ]
    """<p>Information about the change in status for the pull request event.</p>"""
    pull_request_source_reference_updated_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata.PullRequestSourceReferenceUpdatedEventMetadata"
    ]
    """<p>Information about the updated source branch for the pull request event. </p>"""
    pull_request_merged_state_changed_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata.PullRequestMergedStateChangedEventMetadata"
    ]
    """<p>Information about the change in mergability state for the pull request event.</p>"""
    approval_rule_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_event_metadata.ApprovalRuleEventMetadata"
    ]
    """<p>Information about a pull request event.</p>"""
    approval_state_changed_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.approval_state_changed_event_metadata.ApprovalStateChangedEventMetadata"
    ]
    """<p>Information about an approval state change for a pull request.</p>"""
    approval_rule_overridden_event_metadata: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_overridden_event_metadata.ApprovalRuleOverriddenEventMetadata"
    ]
    """<p>Information about an approval rule override event for a pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestEvent) -> dict:
    out: dict = {}
    if "pull_request_id" in value:
        out["pullRequestId"] = value["pull_request_id"]
    if "event_date" in value:
        import aws_sdk_codecommit.types.event_date

        out["eventDate"] = aws_sdk_codecommit.types.event_date.serialize_aws_json_1_1(
            value["event_date"]
        )
    if "pull_request_event_type" in value:
        import aws_sdk_codecommit.types.pull_request_event_type

        out["pullRequestEventType"] = (
            aws_sdk_codecommit.types.pull_request_event_type.serialize_aws_json_1_1(
                value["pull_request_event_type"]
            )
        )
    if "actor_arn" in value:
        out["actorArn"] = value["actor_arn"]
    if "pull_request_created_event_metadata" in value:
        import aws_sdk_codecommit.types.pull_request_created_event_metadata

        out["pullRequestCreatedEventMetadata"] = (
            aws_sdk_codecommit.types.pull_request_created_event_metadata.serialize_aws_json_1_1(
                value["pull_request_created_event_metadata"]
            )
        )
    if "pull_request_status_changed_event_metadata" in value:
        import aws_sdk_codecommit.types.pull_request_status_changed_event_metadata

        out["pullRequestStatusChangedEventMetadata"] = (
            aws_sdk_codecommit.types.pull_request_status_changed_event_metadata.serialize_aws_json_1_1(
                value["pull_request_status_changed_event_metadata"]
            )
        )
    if "pull_request_source_reference_updated_event_metadata" in value:
        import aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata

        out["pullRequestSourceReferenceUpdatedEventMetadata"] = (
            aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata.serialize_aws_json_1_1(
                value["pull_request_source_reference_updated_event_metadata"]
            )
        )
    if "pull_request_merged_state_changed_event_metadata" in value:
        import aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata

        out["pullRequestMergedStateChangedEventMetadata"] = (
            aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata.serialize_aws_json_1_1(
                value["pull_request_merged_state_changed_event_metadata"]
            )
        )
    if "approval_rule_event_metadata" in value:
        import aws_sdk_codecommit.types.approval_rule_event_metadata

        out["approvalRuleEventMetadata"] = (
            aws_sdk_codecommit.types.approval_rule_event_metadata.serialize_aws_json_1_1(
                value["approval_rule_event_metadata"]
            )
        )
    if "approval_state_changed_event_metadata" in value:
        import aws_sdk_codecommit.types.approval_state_changed_event_metadata

        out["approvalStateChangedEventMetadata"] = (
            aws_sdk_codecommit.types.approval_state_changed_event_metadata.serialize_aws_json_1_1(
                value["approval_state_changed_event_metadata"]
            )
        )
    if "approval_rule_overridden_event_metadata" in value:
        import aws_sdk_codecommit.types.approval_rule_overridden_event_metadata

        out["approvalRuleOverriddenEventMetadata"] = (
            aws_sdk_codecommit.types.approval_rule_overridden_event_metadata.serialize_aws_json_1_1(
                value["approval_rule_overridden_event_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestEvent:
    out: PullRequestEvent = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    if "eventDate" in data:
        import aws_sdk_codecommit.types.event_date

        out["event_date"] = (
            aws_sdk_codecommit.types.event_date.deserialize_aws_json_1_1(
                data["eventDate"]
            )
        )
    if "pullRequestEventType" in data:
        import aws_sdk_codecommit.types.pull_request_event_type

        out["pull_request_event_type"] = (
            aws_sdk_codecommit.types.pull_request_event_type.deserialize_aws_json_1_1(
                data["pullRequestEventType"]
            )
        )
    if "actorArn" in data:
        out["actor_arn"] = data["actorArn"]
    if "pullRequestCreatedEventMetadata" in data:
        import aws_sdk_codecommit.types.pull_request_created_event_metadata

        out["pull_request_created_event_metadata"] = (
            aws_sdk_codecommit.types.pull_request_created_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestCreatedEventMetadata"]
            )
        )
    if "pullRequestStatusChangedEventMetadata" in data:
        import aws_sdk_codecommit.types.pull_request_status_changed_event_metadata

        out["pull_request_status_changed_event_metadata"] = (
            aws_sdk_codecommit.types.pull_request_status_changed_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestStatusChangedEventMetadata"]
            )
        )
    if "pullRequestSourceReferenceUpdatedEventMetadata" in data:
        import aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata

        out["pull_request_source_reference_updated_event_metadata"] = (
            aws_sdk_codecommit.types.pull_request_source_reference_updated_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestSourceReferenceUpdatedEventMetadata"]
            )
        )
    if "pullRequestMergedStateChangedEventMetadata" in data:
        import aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata

        out["pull_request_merged_state_changed_event_metadata"] = (
            aws_sdk_codecommit.types.pull_request_merged_state_changed_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestMergedStateChangedEventMetadata"]
            )
        )
    if "approvalRuleEventMetadata" in data:
        import aws_sdk_codecommit.types.approval_rule_event_metadata

        out["approval_rule_event_metadata"] = (
            aws_sdk_codecommit.types.approval_rule_event_metadata.deserialize_aws_json_1_1(
                data["approvalRuleEventMetadata"]
            )
        )
    if "approvalStateChangedEventMetadata" in data:
        import aws_sdk_codecommit.types.approval_state_changed_event_metadata

        out["approval_state_changed_event_metadata"] = (
            aws_sdk_codecommit.types.approval_state_changed_event_metadata.deserialize_aws_json_1_1(
                data["approvalStateChangedEventMetadata"]
            )
        )
    if "approvalRuleOverriddenEventMetadata" in data:
        import aws_sdk_codecommit.types.approval_rule_overridden_event_metadata

        out["approval_rule_overridden_event_metadata"] = (
            aws_sdk_codecommit.types.approval_rule_overridden_event_metadata.deserialize_aws_json_1_1(
                data["approvalRuleOverriddenEventMetadata"]
            )
        )
    return out
