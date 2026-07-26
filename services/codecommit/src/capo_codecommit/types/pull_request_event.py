"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_event_metadata
    import capo_codecommit.types.approval_rule_overridden_event_metadata
    import capo_codecommit.types.approval_state_changed_event_metadata
    import capo_codecommit.types.arn
    import capo_codecommit.types.event_date
    import capo_codecommit.types.pull_request_created_event_metadata
    import capo_codecommit.types.pull_request_event_type
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.pull_request_merged_state_changed_event_metadata
    import capo_codecommit.types.pull_request_source_reference_updated_event_metadata
    import capo_codecommit.types.pull_request_status_changed_event_metadata


class PullRequestEvent(TypedDict, closed=True):
    pull_request_id: NotRequired["capo_codecommit.types.pull_request_id.PullRequestId"]
    """<p>The system-generated ID of the pull request.</p>"""
    event_date: NotRequired["capo_codecommit.types.event_date.EventDate"]
    """<p>The day and time of the pull request event, in timestamp format.</p>"""
    pull_request_event_type: NotRequired[
        "capo_codecommit.types.pull_request_event_type.PullRequestEventType"
    ]
    """<p>The type of the pull request event (for example, a status change event (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED)).</p>"""
    actor_arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.</p>"""
    pull_request_created_event_metadata: NotRequired[
        "capo_codecommit.types.pull_request_created_event_metadata.PullRequestCreatedEventMetadata"
    ]
    """<p>Information about the source and destination branches for the pull request.</p>"""
    pull_request_status_changed_event_metadata: NotRequired[
        "capo_codecommit.types.pull_request_status_changed_event_metadata.PullRequestStatusChangedEventMetadata"
    ]
    """<p>Information about the change in status for the pull request event.</p>"""
    pull_request_source_reference_updated_event_metadata: NotRequired[
        "capo_codecommit.types.pull_request_source_reference_updated_event_metadata.PullRequestSourceReferenceUpdatedEventMetadata"
    ]
    """<p>Information about the updated source branch for the pull request event. </p>"""
    pull_request_merged_state_changed_event_metadata: NotRequired[
        "capo_codecommit.types.pull_request_merged_state_changed_event_metadata.PullRequestMergedStateChangedEventMetadata"
    ]
    """<p>Information about the change in mergability state for the pull request event.</p>"""
    approval_rule_event_metadata: NotRequired[
        "capo_codecommit.types.approval_rule_event_metadata.ApprovalRuleEventMetadata"
    ]
    """<p>Information about a pull request event.</p>"""
    approval_state_changed_event_metadata: NotRequired[
        "capo_codecommit.types.approval_state_changed_event_metadata.ApprovalStateChangedEventMetadata"
    ]
    """<p>Information about an approval state change for a pull request.</p>"""
    approval_rule_overridden_event_metadata: NotRequired[
        "capo_codecommit.types.approval_rule_overridden_event_metadata.ApprovalRuleOverriddenEventMetadata"
    ]
    """<p>Information about an approval rule override event for a pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestEvent) -> dict:
    out: dict = {}
    if "pull_request_id" in value:
        out["pullRequestId"] = value["pull_request_id"]
    if "event_date" in value:
        import capo_codecommit.types.event_date

        out["eventDate"] = capo_codecommit.types.event_date.serialize_aws_json_1_1(
            value["event_date"]
        )
    if "pull_request_event_type" in value:
        import capo_codecommit.types.pull_request_event_type

        out["pullRequestEventType"] = (
            capo_codecommit.types.pull_request_event_type.serialize_aws_json_1_1(
                value["pull_request_event_type"]
            )
        )
    if "actor_arn" in value:
        out["actorArn"] = value["actor_arn"]
    if "pull_request_created_event_metadata" in value:
        import capo_codecommit.types.pull_request_created_event_metadata

        out["pullRequestCreatedEventMetadata"] = (
            capo_codecommit.types.pull_request_created_event_metadata.serialize_aws_json_1_1(
                value["pull_request_created_event_metadata"]
            )
        )
    if "pull_request_status_changed_event_metadata" in value:
        import capo_codecommit.types.pull_request_status_changed_event_metadata

        out["pullRequestStatusChangedEventMetadata"] = (
            capo_codecommit.types.pull_request_status_changed_event_metadata.serialize_aws_json_1_1(
                value["pull_request_status_changed_event_metadata"]
            )
        )
    if "pull_request_source_reference_updated_event_metadata" in value:
        import capo_codecommit.types.pull_request_source_reference_updated_event_metadata

        out["pullRequestSourceReferenceUpdatedEventMetadata"] = (
            capo_codecommit.types.pull_request_source_reference_updated_event_metadata.serialize_aws_json_1_1(
                value["pull_request_source_reference_updated_event_metadata"]
            )
        )
    if "pull_request_merged_state_changed_event_metadata" in value:
        import capo_codecommit.types.pull_request_merged_state_changed_event_metadata

        out["pullRequestMergedStateChangedEventMetadata"] = (
            capo_codecommit.types.pull_request_merged_state_changed_event_metadata.serialize_aws_json_1_1(
                value["pull_request_merged_state_changed_event_metadata"]
            )
        )
    if "approval_rule_event_metadata" in value:
        import capo_codecommit.types.approval_rule_event_metadata

        out["approvalRuleEventMetadata"] = (
            capo_codecommit.types.approval_rule_event_metadata.serialize_aws_json_1_1(
                value["approval_rule_event_metadata"]
            )
        )
    if "approval_state_changed_event_metadata" in value:
        import capo_codecommit.types.approval_state_changed_event_metadata

        out["approvalStateChangedEventMetadata"] = (
            capo_codecommit.types.approval_state_changed_event_metadata.serialize_aws_json_1_1(
                value["approval_state_changed_event_metadata"]
            )
        )
    if "approval_rule_overridden_event_metadata" in value:
        import capo_codecommit.types.approval_rule_overridden_event_metadata

        out["approvalRuleOverriddenEventMetadata"] = (
            capo_codecommit.types.approval_rule_overridden_event_metadata.serialize_aws_json_1_1(
                value["approval_rule_overridden_event_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestEvent:
    out: PullRequestEvent = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    if "eventDate" in data:
        import capo_codecommit.types.event_date

        out["event_date"] = capo_codecommit.types.event_date.deserialize_aws_json_1_1(
            data["eventDate"]
        )
    if "pullRequestEventType" in data:
        import capo_codecommit.types.pull_request_event_type

        out["pull_request_event_type"] = (
            capo_codecommit.types.pull_request_event_type.deserialize_aws_json_1_1(
                data["pullRequestEventType"]
            )
        )
    if "actorArn" in data:
        out["actor_arn"] = data["actorArn"]
    if "pullRequestCreatedEventMetadata" in data:
        import capo_codecommit.types.pull_request_created_event_metadata

        out["pull_request_created_event_metadata"] = (
            capo_codecommit.types.pull_request_created_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestCreatedEventMetadata"]
            )
        )
    if "pullRequestStatusChangedEventMetadata" in data:
        import capo_codecommit.types.pull_request_status_changed_event_metadata

        out["pull_request_status_changed_event_metadata"] = (
            capo_codecommit.types.pull_request_status_changed_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestStatusChangedEventMetadata"]
            )
        )
    if "pullRequestSourceReferenceUpdatedEventMetadata" in data:
        import capo_codecommit.types.pull_request_source_reference_updated_event_metadata

        out["pull_request_source_reference_updated_event_metadata"] = (
            capo_codecommit.types.pull_request_source_reference_updated_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestSourceReferenceUpdatedEventMetadata"]
            )
        )
    if "pullRequestMergedStateChangedEventMetadata" in data:
        import capo_codecommit.types.pull_request_merged_state_changed_event_metadata

        out["pull_request_merged_state_changed_event_metadata"] = (
            capo_codecommit.types.pull_request_merged_state_changed_event_metadata.deserialize_aws_json_1_1(
                data["pullRequestMergedStateChangedEventMetadata"]
            )
        )
    if "approvalRuleEventMetadata" in data:
        import capo_codecommit.types.approval_rule_event_metadata

        out["approval_rule_event_metadata"] = (
            capo_codecommit.types.approval_rule_event_metadata.deserialize_aws_json_1_1(
                data["approvalRuleEventMetadata"]
            )
        )
    if "approvalStateChangedEventMetadata" in data:
        import capo_codecommit.types.approval_state_changed_event_metadata

        out["approval_state_changed_event_metadata"] = (
            capo_codecommit.types.approval_state_changed_event_metadata.deserialize_aws_json_1_1(
                data["approvalStateChangedEventMetadata"]
            )
        )
    if "approvalRuleOverriddenEventMetadata" in data:
        import capo_codecommit.types.approval_rule_overridden_event_metadata

        out["approval_rule_overridden_event_metadata"] = (
            capo_codecommit.types.approval_rule_overridden_event_metadata.deserialize_aws_json_1_1(
                data["approvalRuleOverriddenEventMetadata"]
            )
        )
    return out
