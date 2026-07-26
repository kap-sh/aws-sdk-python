"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.amplitude_connector_profile_properties
    import capo_appflow.types.custom_connector_profile_properties
    import capo_appflow.types.datadog_connector_profile_properties
    import capo_appflow.types.dynatrace_connector_profile_properties
    import capo_appflow.types.google_analytics_connector_profile_properties
    import capo_appflow.types.honeycode_connector_profile_properties
    import capo_appflow.types.infor_nexus_connector_profile_properties
    import capo_appflow.types.marketo_connector_profile_properties
    import capo_appflow.types.pardot_connector_profile_properties
    import capo_appflow.types.redshift_connector_profile_properties
    import capo_appflow.types.salesforce_connector_profile_properties
    import capo_appflow.types.sapo_data_connector_profile_properties
    import capo_appflow.types.service_now_connector_profile_properties
    import capo_appflow.types.singular_connector_profile_properties
    import capo_appflow.types.slack_connector_profile_properties
    import capo_appflow.types.snowflake_connector_profile_properties
    import capo_appflow.types.trendmicro_connector_profile_properties
    import capo_appflow.types.veeva_connector_profile_properties
    import capo_appflow.types.zendesk_connector_profile_properties


class ConnectorProfileProperties(TypedDict, closed=True):
    amplitude: NotRequired[
        "capo_appflow.types.amplitude_connector_profile_properties.AmplitudeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amplitude. </p>"""
    datadog: NotRequired[
        "capo_appflow.types.datadog_connector_profile_properties.DatadogConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Datadog. </p>"""
    dynatrace: NotRequired[
        "capo_appflow.types.dynatrace_connector_profile_properties.DynatraceConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Dynatrace. </p>"""
    google_analytics: NotRequired[
        "capo_appflow.types.google_analytics_connector_profile_properties.GoogleAnalyticsConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required Google Analytics. </p>"""
    honeycode: NotRequired[
        "capo_appflow.types.honeycode_connector_profile_properties.HoneycodeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amazon Honeycode. </p>"""
    infor_nexus: NotRequired[
        "capo_appflow.types.infor_nexus_connector_profile_properties.InforNexusConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Infor Nexus. </p>"""
    marketo: NotRequired[
        "capo_appflow.types.marketo_connector_profile_properties.MarketoConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Marketo. </p>"""
    redshift: NotRequired[
        "capo_appflow.types.redshift_connector_profile_properties.RedshiftConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amazon Redshift. </p>"""
    salesforce: NotRequired[
        "capo_appflow.types.salesforce_connector_profile_properties.SalesforceConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Salesforce. </p>"""
    service_now: NotRequired[
        "capo_appflow.types.service_now_connector_profile_properties.ServiceNowConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by serviceNow. </p>"""
    singular: NotRequired[
        "capo_appflow.types.singular_connector_profile_properties.SingularConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Singular. </p>"""
    slack: NotRequired[
        "capo_appflow.types.slack_connector_profile_properties.SlackConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Slack. </p>"""
    snowflake: NotRequired[
        "capo_appflow.types.snowflake_connector_profile_properties.SnowflakeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Snowflake. </p>"""
    trendmicro: NotRequired[
        "capo_appflow.types.trendmicro_connector_profile_properties.TrendmicroConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Trend Micro. </p>"""
    veeva: NotRequired[
        "capo_appflow.types.veeva_connector_profile_properties.VeevaConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Veeva. </p>"""
    zendesk: NotRequired[
        "capo_appflow.types.zendesk_connector_profile_properties.ZendeskConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Zendesk. </p>"""
    sapo_data: NotRequired[
        "capo_appflow.types.sapo_data_connector_profile_properties.SAPODataConnectorProfileProperties"
    ]
    custom_connector: NotRequired[
        "capo_appflow.types.custom_connector_profile_properties.CustomConnectorProfileProperties"
    ]
    """<p>The properties required by the custom connector.</p>"""
    pardot: NotRequired[
        "capo_appflow.types.pardot_connector_profile_properties.PardotConnectorProfileProperties"
    ]
    """<p>The connector-specific properties required by Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileProperties) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import capo_appflow.types.amplitude_connector_profile_properties

        out["Amplitude"] = (
            capo_appflow.types.amplitude_connector_profile_properties.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import capo_appflow.types.datadog_connector_profile_properties

        out["Datadog"] = (
            capo_appflow.types.datadog_connector_profile_properties.serialize_json(
                value["datadog"]
            )
        )
    if "dynatrace" in value:
        import capo_appflow.types.dynatrace_connector_profile_properties

        out["Dynatrace"] = (
            capo_appflow.types.dynatrace_connector_profile_properties.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import capo_appflow.types.google_analytics_connector_profile_properties

        out["GoogleAnalytics"] = (
            capo_appflow.types.google_analytics_connector_profile_properties.serialize_json(
                value["google_analytics"]
            )
        )
    if "honeycode" in value:
        import capo_appflow.types.honeycode_connector_profile_properties

        out["Honeycode"] = (
            capo_appflow.types.honeycode_connector_profile_properties.serialize_json(
                value["honeycode"]
            )
        )
    if "infor_nexus" in value:
        import capo_appflow.types.infor_nexus_connector_profile_properties

        out["InforNexus"] = (
            capo_appflow.types.infor_nexus_connector_profile_properties.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_connector_profile_properties

        out["Marketo"] = (
            capo_appflow.types.marketo_connector_profile_properties.serialize_json(
                value["marketo"]
            )
        )
    if "redshift" in value:
        import capo_appflow.types.redshift_connector_profile_properties

        out["Redshift"] = (
            capo_appflow.types.redshift_connector_profile_properties.serialize_json(
                value["redshift"]
            )
        )
    if "salesforce" in value:
        import capo_appflow.types.salesforce_connector_profile_properties

        out["Salesforce"] = (
            capo_appflow.types.salesforce_connector_profile_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import capo_appflow.types.service_now_connector_profile_properties

        out["ServiceNow"] = (
            capo_appflow.types.service_now_connector_profile_properties.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import capo_appflow.types.singular_connector_profile_properties

        out["Singular"] = (
            capo_appflow.types.singular_connector_profile_properties.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import capo_appflow.types.slack_connector_profile_properties

        out["Slack"] = (
            capo_appflow.types.slack_connector_profile_properties.serialize_json(
                value["slack"]
            )
        )
    if "snowflake" in value:
        import capo_appflow.types.snowflake_connector_profile_properties

        out["Snowflake"] = (
            capo_appflow.types.snowflake_connector_profile_properties.serialize_json(
                value["snowflake"]
            )
        )
    if "trendmicro" in value:
        import capo_appflow.types.trendmicro_connector_profile_properties

        out["Trendmicro"] = (
            capo_appflow.types.trendmicro_connector_profile_properties.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import capo_appflow.types.veeva_connector_profile_properties

        out["Veeva"] = (
            capo_appflow.types.veeva_connector_profile_properties.serialize_json(
                value["veeva"]
            )
        )
    if "zendesk" in value:
        import capo_appflow.types.zendesk_connector_profile_properties

        out["Zendesk"] = (
            capo_appflow.types.zendesk_connector_profile_properties.serialize_json(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_connector_profile_properties

        out["SAPOData"] = (
            capo_appflow.types.sapo_data_connector_profile_properties.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import capo_appflow.types.custom_connector_profile_properties

        out["CustomConnector"] = (
            capo_appflow.types.custom_connector_profile_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import capo_appflow.types.pardot_connector_profile_properties

        out["Pardot"] = (
            capo_appflow.types.pardot_connector_profile_properties.serialize_json(
                value["pardot"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileProperties:
    out: ConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import capo_appflow.types.amplitude_connector_profile_properties

        out["amplitude"] = (
            capo_appflow.types.amplitude_connector_profile_properties.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import capo_appflow.types.datadog_connector_profile_properties

        out["datadog"] = (
            capo_appflow.types.datadog_connector_profile_properties.deserialize_json(
                data["Datadog"]
            )
        )
    if "Dynatrace" in data:
        import capo_appflow.types.dynatrace_connector_profile_properties

        out["dynatrace"] = (
            capo_appflow.types.dynatrace_connector_profile_properties.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import capo_appflow.types.google_analytics_connector_profile_properties

        out["google_analytics"] = (
            capo_appflow.types.google_analytics_connector_profile_properties.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "Honeycode" in data:
        import capo_appflow.types.honeycode_connector_profile_properties

        out["honeycode"] = (
            capo_appflow.types.honeycode_connector_profile_properties.deserialize_json(
                data["Honeycode"]
            )
        )
    if "InforNexus" in data:
        import capo_appflow.types.infor_nexus_connector_profile_properties

        out["infor_nexus"] = (
            capo_appflow.types.infor_nexus_connector_profile_properties.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import capo_appflow.types.marketo_connector_profile_properties

        out["marketo"] = (
            capo_appflow.types.marketo_connector_profile_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "Redshift" in data:
        import capo_appflow.types.redshift_connector_profile_properties

        out["redshift"] = (
            capo_appflow.types.redshift_connector_profile_properties.deserialize_json(
                data["Redshift"]
            )
        )
    if "Salesforce" in data:
        import capo_appflow.types.salesforce_connector_profile_properties

        out["salesforce"] = (
            capo_appflow.types.salesforce_connector_profile_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import capo_appflow.types.service_now_connector_profile_properties

        out["service_now"] = (
            capo_appflow.types.service_now_connector_profile_properties.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import capo_appflow.types.singular_connector_profile_properties

        out["singular"] = (
            capo_appflow.types.singular_connector_profile_properties.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import capo_appflow.types.slack_connector_profile_properties

        out["slack"] = (
            capo_appflow.types.slack_connector_profile_properties.deserialize_json(
                data["Slack"]
            )
        )
    if "Snowflake" in data:
        import capo_appflow.types.snowflake_connector_profile_properties

        out["snowflake"] = (
            capo_appflow.types.snowflake_connector_profile_properties.deserialize_json(
                data["Snowflake"]
            )
        )
    if "Trendmicro" in data:
        import capo_appflow.types.trendmicro_connector_profile_properties

        out["trendmicro"] = (
            capo_appflow.types.trendmicro_connector_profile_properties.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import capo_appflow.types.veeva_connector_profile_properties

        out["veeva"] = (
            capo_appflow.types.veeva_connector_profile_properties.deserialize_json(
                data["Veeva"]
            )
        )
    if "Zendesk" in data:
        import capo_appflow.types.zendesk_connector_profile_properties

        out["zendesk"] = (
            capo_appflow.types.zendesk_connector_profile_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    if "SAPOData" in data:
        import capo_appflow.types.sapo_data_connector_profile_properties

        out["sapo_data"] = (
            capo_appflow.types.sapo_data_connector_profile_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import capo_appflow.types.custom_connector_profile_properties

        out["custom_connector"] = (
            capo_appflow.types.custom_connector_profile_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "Pardot" in data:
        import capo_appflow.types.pardot_connector_profile_properties

        out["pardot"] = (
            capo_appflow.types.pardot_connector_profile_properties.deserialize_json(
                data["Pardot"]
            )
        )
    return out
