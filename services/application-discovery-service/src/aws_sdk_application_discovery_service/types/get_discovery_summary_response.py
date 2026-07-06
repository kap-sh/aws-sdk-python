"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#GetDiscoverySummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.customer_agent_info
    import aws_sdk_application_discovery_service.types.customer_agentless_collector_info
    import aws_sdk_application_discovery_service.types.customer_connector_info
    import aws_sdk_application_discovery_service.types.customer_me_collector_info
    import aws_sdk_application_discovery_service.types.long


class GetDiscoverySummaryResponse(TypedDict, closed=True):
    servers: "aws_sdk_application_discovery_service.types.long.Long"
    """<p>The number of servers discovered.</p>"""
    applications: "aws_sdk_application_discovery_service.types.long.Long"
    """<p>The number of applications discovered.</p>"""
    servers_mapped_to_applications: (
        "aws_sdk_application_discovery_service.types.long.Long"
    )
    """<p>The number of servers mapped to applications.</p>"""
    servers_mappedto_tags: "aws_sdk_application_discovery_service.types.long.Long"
    """<p>The number of servers mapped to tags.</p>"""
    agent_summary: NotRequired[
        "aws_sdk_application_discovery_service.types.customer_agent_info.CustomerAgentInfo"
    ]
    """<p>Details about discovered agents, including agent status and health.</p>"""
    connector_summary: NotRequired[
        "aws_sdk_application_discovery_service.types.customer_connector_info.CustomerConnectorInfo"
    ]
    """<p>Details about discovered connectors, including connector status and health.</p>"""
    me_collector_summary: NotRequired[
        "aws_sdk_application_discovery_service.types.customer_me_collector_info.CustomerMeCollectorInfo"
    ]
    """<p> Details about Migration Evaluator collectors, including collector status and health. </p>"""
    agentless_collector_summary: NotRequired[
        "aws_sdk_application_discovery_service.types.customer_agentless_collector_info.CustomerAgentlessCollectorInfo"
    ]
    """<p> Details about Agentless Collector collectors, including status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiscoverySummaryResponse) -> dict:
    out: dict = {}
    out["servers"] = value.get("servers", 0)
    out["applications"] = value.get("applications", 0)
    out["serversMappedToApplications"] = value.get("servers_mapped_to_applications", 0)
    out["serversMappedtoTags"] = value.get("servers_mappedto_tags", 0)
    if "agent_summary" in value:
        import aws_sdk_application_discovery_service.types.customer_agent_info

        out["agentSummary"] = (
            aws_sdk_application_discovery_service.types.customer_agent_info.serialize_aws_json_1_1(
                value["agent_summary"]
            )
        )
    if "connector_summary" in value:
        import aws_sdk_application_discovery_service.types.customer_connector_info

        out["connectorSummary"] = (
            aws_sdk_application_discovery_service.types.customer_connector_info.serialize_aws_json_1_1(
                value["connector_summary"]
            )
        )
    if "me_collector_summary" in value:
        import aws_sdk_application_discovery_service.types.customer_me_collector_info

        out["meCollectorSummary"] = (
            aws_sdk_application_discovery_service.types.customer_me_collector_info.serialize_aws_json_1_1(
                value["me_collector_summary"]
            )
        )
    if "agentless_collector_summary" in value:
        import aws_sdk_application_discovery_service.types.customer_agentless_collector_info

        out["agentlessCollectorSummary"] = (
            aws_sdk_application_discovery_service.types.customer_agentless_collector_info.serialize_aws_json_1_1(
                value["agentless_collector_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiscoverySummaryResponse:
    out: GetDiscoverySummaryResponse = {}  # type: ignore[typeddict-item]
    if "servers" in data:
        out["servers"] = data["servers"]
    else:
        out["servers"] = 0
    if "applications" in data:
        out["applications"] = data["applications"]
    else:
        out["applications"] = 0
    if "serversMappedToApplications" in data:
        out["servers_mapped_to_applications"] = data["serversMappedToApplications"]
    else:
        out["servers_mapped_to_applications"] = 0
    if "serversMappedtoTags" in data:
        out["servers_mappedto_tags"] = data["serversMappedtoTags"]
    else:
        out["servers_mappedto_tags"] = 0
    if "agentSummary" in data:
        import aws_sdk_application_discovery_service.types.customer_agent_info

        out["agent_summary"] = (
            aws_sdk_application_discovery_service.types.customer_agent_info.deserialize_aws_json_1_1(
                data["agentSummary"]
            )
        )
    if "connectorSummary" in data:
        import aws_sdk_application_discovery_service.types.customer_connector_info

        out["connector_summary"] = (
            aws_sdk_application_discovery_service.types.customer_connector_info.deserialize_aws_json_1_1(
                data["connectorSummary"]
            )
        )
    if "meCollectorSummary" in data:
        import aws_sdk_application_discovery_service.types.customer_me_collector_info

        out["me_collector_summary"] = (
            aws_sdk_application_discovery_service.types.customer_me_collector_info.deserialize_aws_json_1_1(
                data["meCollectorSummary"]
            )
        )
    if "agentlessCollectorSummary" in data:
        import aws_sdk_application_discovery_service.types.customer_agentless_collector_info

        out["agentless_collector_summary"] = (
            aws_sdk_application_discovery_service.types.customer_agentless_collector_info.deserialize_aws_json_1_1(
                data["agentlessCollectorSummary"]
            )
        )
    return out
