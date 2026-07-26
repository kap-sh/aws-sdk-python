"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rules_list
    import capo_codecommit.types.arn
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.creation_date
    import capo_codecommit.types.description
    import capo_codecommit.types.last_modified_date
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.pull_request_status_enum
    import capo_codecommit.types.pull_request_target_list
    import capo_codecommit.types.revision_id
    import capo_codecommit.types.title


class PullRequest(TypedDict, closed=True):
    pull_request_id: NotRequired["capo_codecommit.types.pull_request_id.PullRequestId"]
    """<p>The system-generated ID of the pull request. </p>"""
    title: NotRequired["capo_codecommit.types.title.Title"]
    """<p>The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.</p>"""
    description: NotRequired["capo_codecommit.types.description.Description"]
    """<p>The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.</p>"""
    last_activity_date: NotRequired[
        "capo_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The day and time of the last user or system activity on the pull request, in timestamp format.</p>"""
    creation_date: NotRequired["capo_codecommit.types.creation_date.CreationDate"]
    """<p>The date and time the pull request was originally created, in timestamp format.</p>"""
    pull_request_status: NotRequired[
        "capo_codecommit.types.pull_request_status_enum.PullRequestStatusEnum"
    ]
    """<p>The status of the pull request. Pull request status can only change from <code>OPEN</code> to <code>CLOSED</code>.</p>"""
    author_arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user who created the pull request.</p>"""
    pull_request_targets: NotRequired[
        "capo_codecommit.types.pull_request_target_list.PullRequestTargetList"
    ]
    """<p>The targets of the pull request, including the source branch and destination branch for the pull request.</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""
    revision_id: NotRequired["capo_codecommit.types.revision_id.RevisionId"]
    """<p>The system-generated revision ID for the pull request.</p>"""
    approval_rules: NotRequired[
        "capo_codecommit.types.approval_rules_list.ApprovalRulesList"
    ]
    """<p>The approval rules applied to the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequest) -> dict:
    out: dict = {}
    if "pull_request_id" in value:
        out["pullRequestId"] = value["pull_request_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_activity_date" in value:
        import capo_codecommit.types.last_modified_date

        out["lastActivityDate"] = (
            capo_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_activity_date"]
            )
        )
    if "creation_date" in value:
        import capo_codecommit.types.creation_date

        out["creationDate"] = (
            capo_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "pull_request_status" in value:
        import capo_codecommit.types.pull_request_status_enum

        out["pullRequestStatus"] = (
            capo_codecommit.types.pull_request_status_enum.serialize_aws_json_1_1(
                value["pull_request_status"]
            )
        )
    if "author_arn" in value:
        out["authorArn"] = value["author_arn"]
    if "pull_request_targets" in value:
        import capo_codecommit.types.pull_request_target_list

        out["pullRequestTargets"] = (
            capo_codecommit.types.pull_request_target_list.serialize_aws_json_1_1(
                value["pull_request_targets"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "approval_rules" in value:
        import capo_codecommit.types.approval_rules_list

        out["approvalRules"] = (
            capo_codecommit.types.approval_rules_list.serialize_aws_json_1_1(
                value["approval_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequest:
    out: PullRequest = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    if "title" in data:
        out["title"] = data["title"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastActivityDate" in data:
        import capo_codecommit.types.last_modified_date

        out["last_activity_date"] = (
            capo_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastActivityDate"]
            )
        )
    if "creationDate" in data:
        import capo_codecommit.types.creation_date

        out["creation_date"] = (
            capo_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "pullRequestStatus" in data:
        import capo_codecommit.types.pull_request_status_enum

        out["pull_request_status"] = (
            capo_codecommit.types.pull_request_status_enum.deserialize_aws_json_1_1(
                data["pullRequestStatus"]
            )
        )
    if "authorArn" in data:
        out["author_arn"] = data["authorArn"]
    if "pullRequestTargets" in data:
        import capo_codecommit.types.pull_request_target_list

        out["pull_request_targets"] = (
            capo_codecommit.types.pull_request_target_list.deserialize_aws_json_1_1(
                data["pullRequestTargets"]
            )
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "approvalRules" in data:
        import capo_codecommit.types.approval_rules_list

        out["approval_rules"] = (
            capo_codecommit.types.approval_rules_list.deserialize_aws_json_1_1(
                data["approvalRules"]
            )
        )
    return out
