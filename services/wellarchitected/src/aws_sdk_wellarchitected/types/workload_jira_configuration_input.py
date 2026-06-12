"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadJiraConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.issue_management_type
    import aws_sdk_wellarchitected.types.jira_project_key
    import aws_sdk_wellarchitected.types.workload_issue_management_status


class WorkloadJiraConfigurationInput(TypedDict):
    issue_management_status: NotRequired[
        "aws_sdk_wellarchitected.types.workload_issue_management_status.WorkloadIssueManagementStatus"
    ]
    """<p>Workload-level: Jira issue management status.</p>"""
    issue_management_type: NotRequired[
        "aws_sdk_wellarchitected.types.issue_management_type.IssueManagementType"
    ]
    """<p>Workload-level: Jira issue management type.</p>"""
    jira_project_key: NotRequired[
        "aws_sdk_wellarchitected.types.jira_project_key.JiraProjectKey"
    ]
    """<p>Workload-level: Jira project key to sync workloads to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadJiraConfigurationInput) -> dict:
    out: dict = {}
    if "issue_management_status" in value:
        import aws_sdk_wellarchitected.types.workload_issue_management_status

        out["IssueManagementStatus"] = (
            aws_sdk_wellarchitected.types.workload_issue_management_status.serialize_json(
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
    return out


def deserialize_json(data: dict) -> WorkloadJiraConfigurationInput:
    out: WorkloadJiraConfigurationInput = {}  # type: ignore[typeddict-item]
    if "IssueManagementStatus" in data:
        import aws_sdk_wellarchitected.types.workload_issue_management_status

        out["issue_management_status"] = (
            aws_sdk_wellarchitected.types.workload_issue_management_status.deserialize_json(
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
    return out
