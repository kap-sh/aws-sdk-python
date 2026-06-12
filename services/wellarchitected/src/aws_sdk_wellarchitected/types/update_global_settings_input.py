"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateGlobalSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.account_jira_configuration_input
    import aws_sdk_wellarchitected.types.discovery_integration_status
    import aws_sdk_wellarchitected.types.organization_sharing_status


class UpdateGlobalSettingsInput(TypedDict):
    organization_sharing_status: NotRequired[
        "aws_sdk_wellarchitected.types.organization_sharing_status.OrganizationSharingStatus"
    ]
    """<p>The status of organization sharing settings.</p>"""
    discovery_integration_status: NotRequired[
        "aws_sdk_wellarchitected.types.discovery_integration_status.DiscoveryIntegrationStatus"
    ]
    """<p>The status of discovery support settings.</p>"""
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.account_jira_configuration_input.AccountJiraConfigurationInput"
    ]
    """<p>The status of Jira integration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalSettingsInput) -> dict:
    out: dict = {}
    if "organization_sharing_status" in value:
        import aws_sdk_wellarchitected.types.organization_sharing_status

        out["OrganizationSharingStatus"] = (
            aws_sdk_wellarchitected.types.organization_sharing_status.serialize_json(
                value["organization_sharing_status"]
            )
        )
    if "discovery_integration_status" in value:
        import aws_sdk_wellarchitected.types.discovery_integration_status

        out["DiscoveryIntegrationStatus"] = (
            aws_sdk_wellarchitected.types.discovery_integration_status.serialize_json(
                value["discovery_integration_status"]
            )
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.account_jira_configuration_input

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.account_jira_configuration_input.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalSettingsInput:
    out: UpdateGlobalSettingsInput = {}  # type: ignore[typeddict-item]
    if "OrganizationSharingStatus" in data:
        import aws_sdk_wellarchitected.types.organization_sharing_status

        out["organization_sharing_status"] = (
            aws_sdk_wellarchitected.types.organization_sharing_status.deserialize_json(
                data["OrganizationSharingStatus"]
            )
        )
    if "DiscoveryIntegrationStatus" in data:
        import aws_sdk_wellarchitected.types.discovery_integration_status

        out["discovery_integration_status"] = (
            aws_sdk_wellarchitected.types.discovery_integration_status.deserialize_json(
                data["DiscoveryIntegrationStatus"]
            )
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.account_jira_configuration_input

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.account_jira_configuration_input.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
