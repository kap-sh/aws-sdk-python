"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountJiraConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_jira_issue_management_status
    import capo_wellarchitected.types.integration_status
    import capo_wellarchitected.types.issue_management_type
    import capo_wellarchitected.types.jira_project_key
    import capo_wellarchitected.types.status_message
    import capo_wellarchitected.types.subdomain


class AccountJiraConfigurationOutput(TypedDict, closed=True):
    integration_status: NotRequired[
        "capo_wellarchitected.types.integration_status.IntegrationStatus"
    ]
    """<p>Account-level: Configuration status of the Jira integration.</p>"""
    issue_management_status: NotRequired[
        "capo_wellarchitected.types.account_jira_issue_management_status.AccountJiraIssueManagementStatus"
    ]
    """<p>Account-level: Jira issue management status.</p>"""
    issue_management_type: NotRequired[
        "capo_wellarchitected.types.issue_management_type.IssueManagementType"
    ]
    """<p>Account-level: Jira issue management type.</p>"""
    subdomain: NotRequired["capo_wellarchitected.types.subdomain.Subdomain"]
    """<p>Account-level: Jira subdomain URL.</p>"""
    jira_project_key: NotRequired[
        "capo_wellarchitected.types.jira_project_key.JiraProjectKey"
    ]
    """<p>Account-level: Jira project key to sync workloads to.</p>"""
    status_message: NotRequired[
        "capo_wellarchitected.types.status_message.StatusMessage"
    ]
    """<p>Account-level: Status message on configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountJiraConfigurationOutput) -> dict:
    out: dict = {}
    if "integration_status" in value:
        import capo_wellarchitected.types.integration_status

        out["IntegrationStatus"] = (
            capo_wellarchitected.types.integration_status.serialize_json(
                value["integration_status"]
            )
        )
    if "issue_management_status" in value:
        import capo_wellarchitected.types.account_jira_issue_management_status

        out["IssueManagementStatus"] = (
            capo_wellarchitected.types.account_jira_issue_management_status.serialize_json(
                value["issue_management_status"]
            )
        )
    if "issue_management_type" in value:
        import capo_wellarchitected.types.issue_management_type

        out["IssueManagementType"] = (
            capo_wellarchitected.types.issue_management_type.serialize_json(
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
        import capo_wellarchitected.types.integration_status

        out["integration_status"] = (
            capo_wellarchitected.types.integration_status.deserialize_json(
                data["IntegrationStatus"]
            )
        )
    if "IssueManagementStatus" in data:
        import capo_wellarchitected.types.account_jira_issue_management_status

        out["issue_management_status"] = (
            capo_wellarchitected.types.account_jira_issue_management_status.deserialize_json(
                data["IssueManagementStatus"]
            )
        )
    if "IssueManagementType" in data:
        import capo_wellarchitected.types.issue_management_type

        out["issue_management_type"] = (
            capo_wellarchitected.types.issue_management_type.deserialize_json(
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
