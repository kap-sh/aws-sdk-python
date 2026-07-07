"""Generated from Smithy shape ``com.amazonaws.devopsagent#AdditionalServiceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details
    import aws_sdk_devops_agent.types.registered_azure_identity_details
    import aws_sdk_devops_agent.types.registered_git_lab_service_details
    import aws_sdk_devops_agent.types.registered_github_service_details
    import aws_sdk_devops_agent.types.registered_grafana_server_details
    import aws_sdk_devops_agent.types.registered_mcp_server_details
    import aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details
    import aws_sdk_devops_agent.types.registered_new_relic_details
    import aws_sdk_devops_agent.types.registered_pager_duty_details
    import aws_sdk_devops_agent.types.registered_service_now_details
    import aws_sdk_devops_agent.types.registered_slack_service_details


class _AdditionalServiceDetails_github(TypedDict, closed=True):
    github: "aws_sdk_devops_agent.types.registered_github_service_details.RegisteredGithubServiceDetails"


class _AdditionalServiceDetails_slack(TypedDict, closed=True):
    slack: "aws_sdk_devops_agent.types.registered_slack_service_details.RegisteredSlackServiceDetails"


class _AdditionalServiceDetails_mcpserverdatadog(TypedDict, closed=True):
    mcpserverdatadog: "aws_sdk_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_mcpserver(TypedDict, closed=True):
    mcpserver: "aws_sdk_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_servicenow(TypedDict, closed=True):
    servicenow: "aws_sdk_devops_agent.types.registered_service_now_details.RegisteredServiceNowDetails"


class _AdditionalServiceDetails_gitlab(TypedDict, closed=True):
    gitlab: "aws_sdk_devops_agent.types.registered_git_lab_service_details.RegisteredGitLabServiceDetails"


class _AdditionalServiceDetails_mcpserversplunk(TypedDict, closed=True):
    mcpserversplunk: "aws_sdk_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_mcpservernewrelic(TypedDict, closed=True):
    mcpservernewrelic: "aws_sdk_devops_agent.types.registered_new_relic_details.RegisteredNewRelicDetails"


class _AdditionalServiceDetails_azuredevops(TypedDict, closed=True):
    azuredevops: "aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details.RegisteredAzureDevOpsServiceDetails"


class _AdditionalServiceDetails_azureidentity(TypedDict, closed=True):
    azureidentity: "aws_sdk_devops_agent.types.registered_azure_identity_details.RegisteredAzureIdentityDetails"


class _AdditionalServiceDetails_mcpservergrafana(TypedDict, closed=True):
    mcpservergrafana: "aws_sdk_devops_agent.types.registered_grafana_server_details.RegisteredGrafanaServerDetails"


class _AdditionalServiceDetails_pagerduty(TypedDict, closed=True):
    pagerduty: "aws_sdk_devops_agent.types.registered_pager_duty_details.RegisteredPagerDutyDetails"


class _AdditionalServiceDetails_mcpserversigv4(TypedDict, closed=True):
    mcpserversigv4: "aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details.RegisteredMCPServerSigV4Details"


AdditionalServiceDetails: TypeAlias = (
    _AdditionalServiceDetails_github
    | _AdditionalServiceDetails_slack
    | _AdditionalServiceDetails_mcpserverdatadog
    | _AdditionalServiceDetails_mcpserver
    | _AdditionalServiceDetails_servicenow
    | _AdditionalServiceDetails_gitlab
    | _AdditionalServiceDetails_mcpserversplunk
    | _AdditionalServiceDetails_mcpservernewrelic
    | _AdditionalServiceDetails_azuredevops
    | _AdditionalServiceDetails_azureidentity
    | _AdditionalServiceDetails_mcpservergrafana
    | _AdditionalServiceDetails_pagerduty
    | _AdditionalServiceDetails_mcpserversigv4
)


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalServiceDetails) -> dict:
    if "github" in value:
        import aws_sdk_devops_agent.types.registered_github_service_details

        return {
            "github": aws_sdk_devops_agent.types.registered_github_service_details.serialize_json(
                value["github"]
            )
        }
    elif "slack" in value:
        import aws_sdk_devops_agent.types.registered_slack_service_details

        return {
            "slack": aws_sdk_devops_agent.types.registered_slack_service_details.serialize_json(
                value["slack"]
            )
        }
    elif "mcpserverdatadog" in value:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserverdatadog": aws_sdk_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in value:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserver": aws_sdk_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserver"]
            )
        }
    elif "servicenow" in value:
        import aws_sdk_devops_agent.types.registered_service_now_details

        return {
            "servicenow": aws_sdk_devops_agent.types.registered_service_now_details.serialize_json(
                value["servicenow"]
            )
        }
    elif "gitlab" in value:
        import aws_sdk_devops_agent.types.registered_git_lab_service_details

        return {
            "gitlab": aws_sdk_devops_agent.types.registered_git_lab_service_details.serialize_json(
                value["gitlab"]
            )
        }
    elif "mcpserversplunk" in value:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserversplunk": aws_sdk_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserversplunk"]
            )
        }
    elif "mcpservernewrelic" in value:
        import aws_sdk_devops_agent.types.registered_new_relic_details

        return {
            "mcpservernewrelic": aws_sdk_devops_agent.types.registered_new_relic_details.serialize_json(
                value["mcpservernewrelic"]
            )
        }
    elif "azuredevops" in value:
        import aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details

        return {
            "azuredevops": aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details.serialize_json(
                value["azuredevops"]
            )
        }
    elif "azureidentity" in value:
        import aws_sdk_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": aws_sdk_devops_agent.types.registered_azure_identity_details.serialize_json(
                value["azureidentity"]
            )
        }
    elif "mcpservergrafana" in value:
        import aws_sdk_devops_agent.types.registered_grafana_server_details

        return {
            "mcpservergrafana": aws_sdk_devops_agent.types.registered_grafana_server_details.serialize_json(
                value["mcpservergrafana"]
            )
        }
    elif "pagerduty" in value:
        import aws_sdk_devops_agent.types.registered_pager_duty_details

        return {
            "pagerduty": aws_sdk_devops_agent.types.registered_pager_duty_details.serialize_json(
                value["pagerduty"]
            )
        }
    elif "mcpserversigv4" in value:
        import aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details

        return {
            "mcpserversigv4": aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details.serialize_json(
                value["mcpserversigv4"]
            )
        }
    else:
        raise SerializationError("AdditionalServiceDetails: no variant present")


def deserialize_json(data: dict) -> AdditionalServiceDetails:
    if "github" in data:
        import aws_sdk_devops_agent.types.registered_github_service_details

        return {
            "github": aws_sdk_devops_agent.types.registered_github_service_details.deserialize_json(
                data["github"]
            )
        }
    elif "slack" in data:
        import aws_sdk_devops_agent.types.registered_slack_service_details

        return {
            "slack": aws_sdk_devops_agent.types.registered_slack_service_details.deserialize_json(
                data["slack"]
            )
        }
    elif "mcpserverdatadog" in data:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserverdatadog": aws_sdk_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in data:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserver": aws_sdk_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserver"]
            )
        }
    elif "servicenow" in data:
        import aws_sdk_devops_agent.types.registered_service_now_details

        return {
            "servicenow": aws_sdk_devops_agent.types.registered_service_now_details.deserialize_json(
                data["servicenow"]
            )
        }
    elif "gitlab" in data:
        import aws_sdk_devops_agent.types.registered_git_lab_service_details

        return {
            "gitlab": aws_sdk_devops_agent.types.registered_git_lab_service_details.deserialize_json(
                data["gitlab"]
            )
        }
    elif "mcpserversplunk" in data:
        import aws_sdk_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserversplunk": aws_sdk_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserversplunk"]
            )
        }
    elif "mcpservernewrelic" in data:
        import aws_sdk_devops_agent.types.registered_new_relic_details

        return {
            "mcpservernewrelic": aws_sdk_devops_agent.types.registered_new_relic_details.deserialize_json(
                data["mcpservernewrelic"]
            )
        }
    elif "azuredevops" in data:
        import aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details

        return {
            "azuredevops": aws_sdk_devops_agent.types.registered_azure_dev_ops_service_details.deserialize_json(
                data["azuredevops"]
            )
        }
    elif "azureidentity" in data:
        import aws_sdk_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": aws_sdk_devops_agent.types.registered_azure_identity_details.deserialize_json(
                data["azureidentity"]
            )
        }
    elif "mcpservergrafana" in data:
        import aws_sdk_devops_agent.types.registered_grafana_server_details

        return {
            "mcpservergrafana": aws_sdk_devops_agent.types.registered_grafana_server_details.deserialize_json(
                data["mcpservergrafana"]
            )
        }
    elif "pagerduty" in data:
        import aws_sdk_devops_agent.types.registered_pager_duty_details

        return {
            "pagerduty": aws_sdk_devops_agent.types.registered_pager_duty_details.deserialize_json(
                data["pagerduty"]
            )
        }
    elif "mcpserversigv4" in data:
        import aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details

        return {
            "mcpserversigv4": aws_sdk_devops_agent.types.registered_mcp_server_sig_v4_details.deserialize_json(
                data["mcpserversigv4"]
            )
        }
    else:
        raise DeserializationError(
            "AdditionalServiceDetails: no recognized variant key"
        )
