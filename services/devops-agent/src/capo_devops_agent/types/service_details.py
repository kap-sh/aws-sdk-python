"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.datadog_service_details
    import capo_devops_agent.types.dynatrace_service_details
    import capo_devops_agent.types.event_channel_details
    import capo_devops_agent.types.git_lab_details
    import capo_devops_agent.types.grafana_service_details
    import capo_devops_agent.types.mcp_server_details
    import capo_devops_agent.types.mcp_server_sig_v4_service_details
    import capo_devops_agent.types.new_relic_service_details
    import capo_devops_agent.types.pager_duty_details
    import capo_devops_agent.types.registered_azure_identity_details
    import capo_devops_agent.types.service_now_service_details


class _ServiceDetails_dynatrace(TypedDict, closed=True):
    dynatrace: (
        "capo_devops_agent.types.dynatrace_service_details.DynatraceServiceDetails"
    )


class _ServiceDetails_servicenow(TypedDict, closed=True):
    servicenow: (
        "capo_devops_agent.types.service_now_service_details.ServiceNowServiceDetails"
    )


class _ServiceDetails_mcpserverdatadog(TypedDict, closed=True):
    mcpserverdatadog: (
        "capo_devops_agent.types.datadog_service_details.DatadogServiceDetails"
    )


class _ServiceDetails_mcpserver(TypedDict, closed=True):
    mcpserver: "capo_devops_agent.types.mcp_server_details.MCPServerDetails"


class _ServiceDetails_gitlab(TypedDict, closed=True):
    gitlab: "capo_devops_agent.types.git_lab_details.GitLabDetails"


class _ServiceDetails_mcpserversplunk(TypedDict, closed=True):
    mcpserversplunk: "capo_devops_agent.types.mcp_server_details.MCPServerDetails"


class _ServiceDetails_mcpservernewrelic(TypedDict, closed=True):
    mcpservernewrelic: (
        "capo_devops_agent.types.new_relic_service_details.NewRelicServiceDetails"
    )


class _ServiceDetails_eventChannel(TypedDict, closed=True):
    eventChannel: "capo_devops_agent.types.event_channel_details.EventChannelDetails"


class _ServiceDetails_mcpservergrafana(TypedDict, closed=True):
    mcpservergrafana: (
        "capo_devops_agent.types.grafana_service_details.GrafanaServiceDetails"
    )


class _ServiceDetails_pagerduty(TypedDict, closed=True):
    pagerduty: "capo_devops_agent.types.pager_duty_details.PagerDutyDetails"


class _ServiceDetails_azureidentity(TypedDict, closed=True):
    azureidentity: "capo_devops_agent.types.registered_azure_identity_details.RegisteredAzureIdentityDetails"


class _ServiceDetails_mcpserversigv4(TypedDict, closed=True):
    mcpserversigv4: "capo_devops_agent.types.mcp_server_sig_v4_service_details.MCPServerSigV4ServiceDetails"


ServiceDetails: TypeAlias = (
    _ServiceDetails_dynatrace
    | _ServiceDetails_servicenow
    | _ServiceDetails_mcpserverdatadog
    | _ServiceDetails_mcpserver
    | _ServiceDetails_gitlab
    | _ServiceDetails_mcpserversplunk
    | _ServiceDetails_mcpservernewrelic
    | _ServiceDetails_eventChannel
    | _ServiceDetails_mcpservergrafana
    | _ServiceDetails_pagerduty
    | _ServiceDetails_azureidentity
    | _ServiceDetails_mcpserversigv4
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDetails) -> dict:
    if "dynatrace" in value:
        import capo_devops_agent.types.dynatrace_service_details

        return {
            "dynatrace": capo_devops_agent.types.dynatrace_service_details.serialize_json(
                value["dynatrace"]
            )
        }
    elif "servicenow" in value:
        import capo_devops_agent.types.service_now_service_details

        return {
            "servicenow": capo_devops_agent.types.service_now_service_details.serialize_json(
                value["servicenow"]
            )
        }
    elif "mcpserverdatadog" in value:
        import capo_devops_agent.types.datadog_service_details

        return {
            "mcpserverdatadog": capo_devops_agent.types.datadog_service_details.serialize_json(
                value["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in value:
        import capo_devops_agent.types.mcp_server_details

        return {
            "mcpserver": capo_devops_agent.types.mcp_server_details.serialize_json(
                value["mcpserver"]
            )
        }
    elif "gitlab" in value:
        import capo_devops_agent.types.git_lab_details

        return {
            "gitlab": capo_devops_agent.types.git_lab_details.serialize_json(
                value["gitlab"]
            )
        }
    elif "mcpserversplunk" in value:
        import capo_devops_agent.types.mcp_server_details

        return {
            "mcpserversplunk": capo_devops_agent.types.mcp_server_details.serialize_json(
                value["mcpserversplunk"]
            )
        }
    elif "mcpservernewrelic" in value:
        import capo_devops_agent.types.new_relic_service_details

        return {
            "mcpservernewrelic": capo_devops_agent.types.new_relic_service_details.serialize_json(
                value["mcpservernewrelic"]
            )
        }
    elif "eventChannel" in value:
        import capo_devops_agent.types.event_channel_details

        return {
            "eventChannel": capo_devops_agent.types.event_channel_details.serialize_json(
                value["eventChannel"]
            )
        }
    elif "mcpservergrafana" in value:
        import capo_devops_agent.types.grafana_service_details

        return {
            "mcpservergrafana": capo_devops_agent.types.grafana_service_details.serialize_json(
                value["mcpservergrafana"]
            )
        }
    elif "pagerduty" in value:
        import capo_devops_agent.types.pager_duty_details

        return {
            "pagerduty": capo_devops_agent.types.pager_duty_details.serialize_json(
                value["pagerduty"]
            )
        }
    elif "azureidentity" in value:
        import capo_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": capo_devops_agent.types.registered_azure_identity_details.serialize_json(
                value["azureidentity"]
            )
        }
    elif "mcpserversigv4" in value:
        import capo_devops_agent.types.mcp_server_sig_v4_service_details

        return {
            "mcpserversigv4": capo_devops_agent.types.mcp_server_sig_v4_service_details.serialize_json(
                value["mcpserversigv4"]
            )
        }
    else:
        raise SerializationError("ServiceDetails: no variant present")


def deserialize_json(data: dict) -> ServiceDetails:
    if "dynatrace" in data:
        import capo_devops_agent.types.dynatrace_service_details

        return {
            "dynatrace": capo_devops_agent.types.dynatrace_service_details.deserialize_json(
                data["dynatrace"]
            )
        }
    elif "servicenow" in data:
        import capo_devops_agent.types.service_now_service_details

        return {
            "servicenow": capo_devops_agent.types.service_now_service_details.deserialize_json(
                data["servicenow"]
            )
        }
    elif "mcpserverdatadog" in data:
        import capo_devops_agent.types.datadog_service_details

        return {
            "mcpserverdatadog": capo_devops_agent.types.datadog_service_details.deserialize_json(
                data["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in data:
        import capo_devops_agent.types.mcp_server_details

        return {
            "mcpserver": capo_devops_agent.types.mcp_server_details.deserialize_json(
                data["mcpserver"]
            )
        }
    elif "gitlab" in data:
        import capo_devops_agent.types.git_lab_details

        return {
            "gitlab": capo_devops_agent.types.git_lab_details.deserialize_json(
                data["gitlab"]
            )
        }
    elif "mcpserversplunk" in data:
        import capo_devops_agent.types.mcp_server_details

        return {
            "mcpserversplunk": capo_devops_agent.types.mcp_server_details.deserialize_json(
                data["mcpserversplunk"]
            )
        }
    elif "mcpservernewrelic" in data:
        import capo_devops_agent.types.new_relic_service_details

        return {
            "mcpservernewrelic": capo_devops_agent.types.new_relic_service_details.deserialize_json(
                data["mcpservernewrelic"]
            )
        }
    elif "eventChannel" in data:
        import capo_devops_agent.types.event_channel_details

        return {
            "eventChannel": capo_devops_agent.types.event_channel_details.deserialize_json(
                data["eventChannel"]
            )
        }
    elif "mcpservergrafana" in data:
        import capo_devops_agent.types.grafana_service_details

        return {
            "mcpservergrafana": capo_devops_agent.types.grafana_service_details.deserialize_json(
                data["mcpservergrafana"]
            )
        }
    elif "pagerduty" in data:
        import capo_devops_agent.types.pager_duty_details

        return {
            "pagerduty": capo_devops_agent.types.pager_duty_details.deserialize_json(
                data["pagerduty"]
            )
        }
    elif "azureidentity" in data:
        import capo_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": capo_devops_agent.types.registered_azure_identity_details.deserialize_json(
                data["azureidentity"]
            )
        }
    elif "mcpserversigv4" in data:
        import capo_devops_agent.types.mcp_server_sig_v4_service_details

        return {
            "mcpserversigv4": capo_devops_agent.types.mcp_server_sig_v4_service_details.deserialize_json(
                data["mcpserversigv4"]
            )
        }
    else:
        raise DeserializationError("ServiceDetails: no recognized variant key")
