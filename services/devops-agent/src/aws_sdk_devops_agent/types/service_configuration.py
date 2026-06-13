"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.aws_configuration
    import aws_sdk_devops_agent.types.azure_configuration
    import aws_sdk_devops_agent.types.azure_dev_ops_configuration
    import aws_sdk_devops_agent.types.dynatrace_configuration
    import aws_sdk_devops_agent.types.event_channel_configuration
    import aws_sdk_devops_agent.types.git_hub_configuration
    import aws_sdk_devops_agent.types.git_lab_configuration
    import aws_sdk_devops_agent.types.mcp_server_configuration
    import aws_sdk_devops_agent.types.mcp_server_datadog_configuration
    import aws_sdk_devops_agent.types.mcp_server_grafana_configuration
    import aws_sdk_devops_agent.types.mcp_server_new_relic_configuration
    import aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration
    import aws_sdk_devops_agent.types.mcp_server_splunk_configuration
    import aws_sdk_devops_agent.types.pager_duty_configuration
    import aws_sdk_devops_agent.types.service_now_configuration
    import aws_sdk_devops_agent.types.slack_configuration
    import aws_sdk_devops_agent.types.source_aws_configuration


class _ServiceConfiguration_sourceAws(TypedDict):
    sourceAws: (
        "aws_sdk_devops_agent.types.source_aws_configuration.SourceAwsConfiguration"
    )


class _ServiceConfiguration_aws(TypedDict):
    aws: "aws_sdk_devops_agent.types.aws_configuration.AWSConfiguration"


class _ServiceConfiguration_github(TypedDict):
    github: "aws_sdk_devops_agent.types.git_hub_configuration.GitHubConfiguration"


class _ServiceConfiguration_slack(TypedDict):
    slack: "aws_sdk_devops_agent.types.slack_configuration.SlackConfiguration"


class _ServiceConfiguration_dynatrace(TypedDict):
    dynatrace: (
        "aws_sdk_devops_agent.types.dynatrace_configuration.DynatraceConfiguration"
    )


class _ServiceConfiguration_servicenow(TypedDict):
    servicenow: (
        "aws_sdk_devops_agent.types.service_now_configuration.ServiceNowConfiguration"
    )


class _ServiceConfiguration_mcpservernewrelic(TypedDict):
    mcpservernewrelic: "aws_sdk_devops_agent.types.mcp_server_new_relic_configuration.MCPServerNewRelicConfiguration"


class _ServiceConfiguration_mcpserverdatadog(TypedDict):
    mcpserverdatadog: "aws_sdk_devops_agent.types.mcp_server_datadog_configuration.MCPServerDatadogConfiguration"


class _ServiceConfiguration_mcpserver(TypedDict):
    mcpserver: (
        "aws_sdk_devops_agent.types.mcp_server_configuration.MCPServerConfiguration"
    )


class _ServiceConfiguration_gitlab(TypedDict):
    gitlab: "aws_sdk_devops_agent.types.git_lab_configuration.GitLabConfiguration"


class _ServiceConfiguration_mcpserversplunk(TypedDict):
    mcpserversplunk: "aws_sdk_devops_agent.types.mcp_server_splunk_configuration.MCPServerSplunkConfiguration"


class _ServiceConfiguration_eventChannel(TypedDict):
    eventChannel: "aws_sdk_devops_agent.types.event_channel_configuration.EventChannelConfiguration"


class _ServiceConfiguration_azure(TypedDict):
    azure: "aws_sdk_devops_agent.types.azure_configuration.AzureConfiguration"


class _ServiceConfiguration_azuredevops(TypedDict):
    azuredevops: "aws_sdk_devops_agent.types.azure_dev_ops_configuration.AzureDevOpsConfiguration"


class _ServiceConfiguration_mcpservergrafana(TypedDict):
    mcpservergrafana: "aws_sdk_devops_agent.types.mcp_server_grafana_configuration.MCPServerGrafanaConfiguration"


class _ServiceConfiguration_pagerduty(TypedDict):
    pagerduty: (
        "aws_sdk_devops_agent.types.pager_duty_configuration.PagerDutyConfiguration"
    )


class _ServiceConfiguration_mcpserversigv4(TypedDict):
    mcpserversigv4: "aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration.MCPServerSigV4Configuration"


ServiceConfiguration: TypeAlias = (
    _ServiceConfiguration_sourceAws
    | _ServiceConfiguration_aws
    | _ServiceConfiguration_github
    | _ServiceConfiguration_slack
    | _ServiceConfiguration_dynatrace
    | _ServiceConfiguration_servicenow
    | _ServiceConfiguration_mcpservernewrelic
    | _ServiceConfiguration_mcpserverdatadog
    | _ServiceConfiguration_mcpserver
    | _ServiceConfiguration_gitlab
    | _ServiceConfiguration_mcpserversplunk
    | _ServiceConfiguration_eventChannel
    | _ServiceConfiguration_azure
    | _ServiceConfiguration_azuredevops
    | _ServiceConfiguration_mcpservergrafana
    | _ServiceConfiguration_pagerduty
    | _ServiceConfiguration_mcpserversigv4
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceConfiguration) -> dict:
    if "sourceAws" in value:
        import aws_sdk_devops_agent.types.source_aws_configuration

        return {
            "sourceAws": aws_sdk_devops_agent.types.source_aws_configuration.serialize_json(
                value["sourceAws"]
            )
        }
    elif "aws" in value:
        import aws_sdk_devops_agent.types.aws_configuration

        return {
            "aws": aws_sdk_devops_agent.types.aws_configuration.serialize_json(
                value["aws"]
            )
        }
    elif "github" in value:
        import aws_sdk_devops_agent.types.git_hub_configuration

        return {
            "github": aws_sdk_devops_agent.types.git_hub_configuration.serialize_json(
                value["github"]
            )
        }
    elif "slack" in value:
        import aws_sdk_devops_agent.types.slack_configuration

        return {
            "slack": aws_sdk_devops_agent.types.slack_configuration.serialize_json(
                value["slack"]
            )
        }
    elif "dynatrace" in value:
        import aws_sdk_devops_agent.types.dynatrace_configuration

        return {
            "dynatrace": aws_sdk_devops_agent.types.dynatrace_configuration.serialize_json(
                value["dynatrace"]
            )
        }
    elif "servicenow" in value:
        import aws_sdk_devops_agent.types.service_now_configuration

        return {
            "servicenow": aws_sdk_devops_agent.types.service_now_configuration.serialize_json(
                value["servicenow"]
            )
        }
    elif "mcpservernewrelic" in value:
        import aws_sdk_devops_agent.types.mcp_server_new_relic_configuration

        return {
            "mcpservernewrelic": aws_sdk_devops_agent.types.mcp_server_new_relic_configuration.serialize_json(
                value["mcpservernewrelic"]
            )
        }
    elif "mcpserverdatadog" in value:
        import aws_sdk_devops_agent.types.mcp_server_datadog_configuration

        return {
            "mcpserverdatadog": aws_sdk_devops_agent.types.mcp_server_datadog_configuration.serialize_json(
                value["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in value:
        import aws_sdk_devops_agent.types.mcp_server_configuration

        return {
            "mcpserver": aws_sdk_devops_agent.types.mcp_server_configuration.serialize_json(
                value["mcpserver"]
            )
        }
    elif "gitlab" in value:
        import aws_sdk_devops_agent.types.git_lab_configuration

        return {
            "gitlab": aws_sdk_devops_agent.types.git_lab_configuration.serialize_json(
                value["gitlab"]
            )
        }
    elif "mcpserversplunk" in value:
        import aws_sdk_devops_agent.types.mcp_server_splunk_configuration

        return {
            "mcpserversplunk": aws_sdk_devops_agent.types.mcp_server_splunk_configuration.serialize_json(
                value["mcpserversplunk"]
            )
        }
    elif "eventChannel" in value:
        import aws_sdk_devops_agent.types.event_channel_configuration

        return {
            "eventChannel": aws_sdk_devops_agent.types.event_channel_configuration.serialize_json(
                value["eventChannel"]
            )
        }
    elif "azure" in value:
        import aws_sdk_devops_agent.types.azure_configuration

        return {
            "azure": aws_sdk_devops_agent.types.azure_configuration.serialize_json(
                value["azure"]
            )
        }
    elif "azuredevops" in value:
        import aws_sdk_devops_agent.types.azure_dev_ops_configuration

        return {
            "azuredevops": aws_sdk_devops_agent.types.azure_dev_ops_configuration.serialize_json(
                value["azuredevops"]
            )
        }
    elif "mcpservergrafana" in value:
        import aws_sdk_devops_agent.types.mcp_server_grafana_configuration

        return {
            "mcpservergrafana": aws_sdk_devops_agent.types.mcp_server_grafana_configuration.serialize_json(
                value["mcpservergrafana"]
            )
        }
    elif "pagerduty" in value:
        import aws_sdk_devops_agent.types.pager_duty_configuration

        return {
            "pagerduty": aws_sdk_devops_agent.types.pager_duty_configuration.serialize_json(
                value["pagerduty"]
            )
        }
    elif "mcpserversigv4" in value:
        import aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration

        return {
            "mcpserversigv4": aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration.serialize_json(
                value["mcpserversigv4"]
            )
        }
    else:
        raise SerializationError("ServiceConfiguration: no variant present")


def deserialize_json(data: dict) -> ServiceConfiguration:
    if "sourceAws" in data:
        import aws_sdk_devops_agent.types.source_aws_configuration

        return {
            "sourceAws": aws_sdk_devops_agent.types.source_aws_configuration.deserialize_json(
                data["sourceAws"]
            )
        }
    elif "aws" in data:
        import aws_sdk_devops_agent.types.aws_configuration

        return {
            "aws": aws_sdk_devops_agent.types.aws_configuration.deserialize_json(
                data["aws"]
            )
        }
    elif "github" in data:
        import aws_sdk_devops_agent.types.git_hub_configuration

        return {
            "github": aws_sdk_devops_agent.types.git_hub_configuration.deserialize_json(
                data["github"]
            )
        }
    elif "slack" in data:
        import aws_sdk_devops_agent.types.slack_configuration

        return {
            "slack": aws_sdk_devops_agent.types.slack_configuration.deserialize_json(
                data["slack"]
            )
        }
    elif "dynatrace" in data:
        import aws_sdk_devops_agent.types.dynatrace_configuration

        return {
            "dynatrace": aws_sdk_devops_agent.types.dynatrace_configuration.deserialize_json(
                data["dynatrace"]
            )
        }
    elif "servicenow" in data:
        import aws_sdk_devops_agent.types.service_now_configuration

        return {
            "servicenow": aws_sdk_devops_agent.types.service_now_configuration.deserialize_json(
                data["servicenow"]
            )
        }
    elif "mcpservernewrelic" in data:
        import aws_sdk_devops_agent.types.mcp_server_new_relic_configuration

        return {
            "mcpservernewrelic": aws_sdk_devops_agent.types.mcp_server_new_relic_configuration.deserialize_json(
                data["mcpservernewrelic"]
            )
        }
    elif "mcpserverdatadog" in data:
        import aws_sdk_devops_agent.types.mcp_server_datadog_configuration

        return {
            "mcpserverdatadog": aws_sdk_devops_agent.types.mcp_server_datadog_configuration.deserialize_json(
                data["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in data:
        import aws_sdk_devops_agent.types.mcp_server_configuration

        return {
            "mcpserver": aws_sdk_devops_agent.types.mcp_server_configuration.deserialize_json(
                data["mcpserver"]
            )
        }
    elif "gitlab" in data:
        import aws_sdk_devops_agent.types.git_lab_configuration

        return {
            "gitlab": aws_sdk_devops_agent.types.git_lab_configuration.deserialize_json(
                data["gitlab"]
            )
        }
    elif "mcpserversplunk" in data:
        import aws_sdk_devops_agent.types.mcp_server_splunk_configuration

        return {
            "mcpserversplunk": aws_sdk_devops_agent.types.mcp_server_splunk_configuration.deserialize_json(
                data["mcpserversplunk"]
            )
        }
    elif "eventChannel" in data:
        import aws_sdk_devops_agent.types.event_channel_configuration

        return {
            "eventChannel": aws_sdk_devops_agent.types.event_channel_configuration.deserialize_json(
                data["eventChannel"]
            )
        }
    elif "azure" in data:
        import aws_sdk_devops_agent.types.azure_configuration

        return {
            "azure": aws_sdk_devops_agent.types.azure_configuration.deserialize_json(
                data["azure"]
            )
        }
    elif "azuredevops" in data:
        import aws_sdk_devops_agent.types.azure_dev_ops_configuration

        return {
            "azuredevops": aws_sdk_devops_agent.types.azure_dev_ops_configuration.deserialize_json(
                data["azuredevops"]
            )
        }
    elif "mcpservergrafana" in data:
        import aws_sdk_devops_agent.types.mcp_server_grafana_configuration

        return {
            "mcpservergrafana": aws_sdk_devops_agent.types.mcp_server_grafana_configuration.deserialize_json(
                data["mcpservergrafana"]
            )
        }
    elif "pagerduty" in data:
        import aws_sdk_devops_agent.types.pager_duty_configuration

        return {
            "pagerduty": aws_sdk_devops_agent.types.pager_duty_configuration.deserialize_json(
                data["pagerduty"]
            )
        }
    elif "mcpserversigv4" in data:
        import aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration

        return {
            "mcpserversigv4": aws_sdk_devops_agent.types.mcp_server_sig_v4_configuration.deserialize_json(
                data["mcpserversigv4"]
            )
        }
    else:
        raise DeserializationError("ServiceConfiguration: no recognized variant key")
