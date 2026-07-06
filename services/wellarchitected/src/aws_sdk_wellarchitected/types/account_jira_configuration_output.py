"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountJiraConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.account_jira_issue_management_status
    import aws_sdk_wellarchitected.types.integration_status
    import aws_sdk_wellarchitected.types.issue_management_type
    import aws_sdk_wellarchitected.types.jira_project_key
    import aws_sdk_wellarchitected.types.status_message
    import aws_sdk_wellarchitected.types.subdomain


class AccountJiraConfigurationOutput(TypedDict, closed=True):
    integration_status: NotRequired[
        "aws_sdk_wellarchitected.types.integration_status.IntegrationStatus"
    ]
    """<p>Account-level: Configuration status of the Jira integration.</p>"""
    issue_management_status: NotRequired[
        "aws_sdk_wellarchitected.types.account_jira_issue_management_status.AccountJiraIssueManagementStatus"
    ]
    """<p>Account-level: Jira issue management status.</p>"""
    issue_management_type: NotRequired[
        "aws_sdk_wellarchitected.types.issue_management_type.IssueManagementType"
    ]
    """<p>Account-level: Jira issue management type.</p>"""
    subdomain: NotRequired["aws_sdk_wellarchitected.types.subdomain.Subdomain"]
    """<p>Account-level: Jira subdomain URL.</p>"""
    jira_project_key: NotRequired[
        "aws_sdk_wellarchitected.types.jira_project_key.JiraProjectKey"
    ]
    """<p>Account-level: Jira project key to sync workloads to.</p>"""
    status_message: NotRequired[
        "aws_sdk_wellarchitected.types.status_message.StatusMessage"
    ]
    """<p>Account-level: Status message on configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountJiraConfigurationOutput) -> dict:
    out: dict = {}
    if "integration_status" in value:
        import aws_sdk_wellarchitected.types.integration_status

        out["IntegrationStatus"] = (
            aws_sdk_wellarchitected.types.integration_status.serialize_json(
                value["integration_status"]
            )
        )
    if "issue_management_status" in value:
        import aws_sdk_wellarchitected.types.account_jira_issue_management_status

        out["IssueManagementStatus"] = (
            aws_sdk_wellarchitected.types.account_jira_issue_management_status.serialize_json(
                value["issue_management_status"]
            )
        )
    if "issue_management_type" in value:
        import aws_sdk_wellarchitected.types.issue_management_type

        out["IssueManagementType"] = (
            aws_sdk_wellarchitected.types.issue_management_type.serialize_json(
                value["issue_management_type"]
            )
        )
    if "subdomain" in value:
        out["Subdomain"] = value["subdomain"]
    if "jira_project_key" in value:
        out["JiraProjectKey"] = value["jira_project_key"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> AccountJiraConfigurationOutput:
    out: AccountJiraConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "IntegrationStatus" in data:
        import aws_sdk_wellarchitected.types.integration_status

        out["integration_status"] = (
            aws_sdk_wellarchitected.types.integration_status.deserialize_json(
                data["IntegrationStatus"]
            )
        )
    if "IssueManagementStatus" in data:
        import aws_sdk_wellarchitected.types.account_jira_issue_management_status

        out["issue_management_status"] = (
            aws_sdk_wellarchitected.types.account_jira_issue_management_status.deserialize_json(
                data["IssueManagementStatus"]
            )
        )
    if "IssueManagementType" in data:
        import aws_sdk_wellarchitected.types.issue_management_type

        out["issue_management_type"] = (
            aws_sdk_wellarchitected.types.issue_management_type.deserialize_json(
                data["IssueManagementType"]
            )
        )
    if "Subdomain" in data:
        out["subdomain"] = data["Subdomain"]
    if "JiraProjectKey" in data:
        out["jira_project_key"] = data["JiraProjectKey"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
