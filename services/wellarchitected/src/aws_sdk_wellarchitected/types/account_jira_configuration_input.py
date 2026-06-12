"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountJiraConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.account_jira_issue_management_status
    import aws_sdk_wellarchitected.types.integration_status_input
    import aws_sdk_wellarchitected.types.issue_management_type
    import aws_sdk_wellarchitected.types.jira_project_key


class AccountJiraConfigurationInput(TypedDict):
    issue_management_status: NotRequired[
        "aws_sdk_wellarchitected.types.account_jira_issue_management_status.AccountJiraIssueManagementStatus"
    ]
    """<p>Account-level: Jira issue management status.</p>"""
    issue_management_type: NotRequired[
        "aws_sdk_wellarchitected.types.issue_management_type.IssueManagementType"
    ]
    """<p>Account-level: Jira issue management type.</p>"""
    jira_project_key: NotRequired[
        "aws_sdk_wellarchitected.types.jira_project_key.JiraProjectKey"
    ]
    """<p>Account-level: Jira project key to sync workloads to.</p>"""
    integration_status: NotRequired[
        "aws_sdk_wellarchitected.types.integration_status_input.IntegrationStatusInput"
    ]
    """<p>Account-level: Configuration status of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountJiraConfigurationInput) -> dict:
    out: dict = {}
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
    if "jira_project_key" in value:
        out["JiraProjectKey"] = value["jira_project_key"]
    if "integration_status" in value:
        import aws_sdk_wellarchitected.types.integration_status_input

        out["IntegrationStatus"] = (
            aws_sdk_wellarchitected.types.integration_status_input.serialize_json(
                value["integration_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountJiraConfigurationInput:
    out: AccountJiraConfigurationInput = {}  # type: ignore[typeddict-item]
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
    if "JiraProjectKey" in data:
        out["jira_project_key"] = data["JiraProjectKey"]
    if "IntegrationStatus" in data:
        import aws_sdk_wellarchitected.types.integration_status_input

        out["integration_status"] = (
            aws_sdk_wellarchitected.types.integration_status_input.deserialize_json(
                data["IntegrationStatus"]
            )
        )
    return out
