"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.amplitude_connector_profile_properties
    import aws_sdk_appflow.types.custom_connector_profile_properties
    import aws_sdk_appflow.types.datadog_connector_profile_properties
    import aws_sdk_appflow.types.dynatrace_connector_profile_properties
    import aws_sdk_appflow.types.google_analytics_connector_profile_properties
    import aws_sdk_appflow.types.honeycode_connector_profile_properties
    import aws_sdk_appflow.types.infor_nexus_connector_profile_properties
    import aws_sdk_appflow.types.marketo_connector_profile_properties
    import aws_sdk_appflow.types.pardot_connector_profile_properties
    import aws_sdk_appflow.types.redshift_connector_profile_properties
    import aws_sdk_appflow.types.salesforce_connector_profile_properties
    import aws_sdk_appflow.types.sapo_data_connector_profile_properties
    import aws_sdk_appflow.types.service_now_connector_profile_properties
    import aws_sdk_appflow.types.singular_connector_profile_properties
    import aws_sdk_appflow.types.slack_connector_profile_properties
    import aws_sdk_appflow.types.snowflake_connector_profile_properties
    import aws_sdk_appflow.types.trendmicro_connector_profile_properties
    import aws_sdk_appflow.types.veeva_connector_profile_properties
    import aws_sdk_appflow.types.zendesk_connector_profile_properties


class ConnectorProfileProperties(TypedDict):
    amplitude: NotRequired[
        "aws_sdk_appflow.types.amplitude_connector_profile_properties.AmplitudeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amplitude. </p>"""
    datadog: NotRequired[
        "aws_sdk_appflow.types.datadog_connector_profile_properties.DatadogConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Datadog. </p>"""
    dynatrace: NotRequired[
        "aws_sdk_appflow.types.dynatrace_connector_profile_properties.DynatraceConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Dynatrace. </p>"""
    google_analytics: NotRequired[
        "aws_sdk_appflow.types.google_analytics_connector_profile_properties.GoogleAnalyticsConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required Google Analytics. </p>"""
    honeycode: NotRequired[
        "aws_sdk_appflow.types.honeycode_connector_profile_properties.HoneycodeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amazon Honeycode. </p>"""
    infor_nexus: NotRequired[
        "aws_sdk_appflow.types.infor_nexus_connector_profile_properties.InforNexusConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Infor Nexus. </p>"""
    marketo: NotRequired[
        "aws_sdk_appflow.types.marketo_connector_profile_properties.MarketoConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Marketo. </p>"""
    redshift: NotRequired[
        "aws_sdk_appflow.types.redshift_connector_profile_properties.RedshiftConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Amazon Redshift. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_connector_profile_properties.SalesforceConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Salesforce. </p>"""
    service_now: NotRequired[
        "aws_sdk_appflow.types.service_now_connector_profile_properties.ServiceNowConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by serviceNow. </p>"""
    singular: NotRequired[
        "aws_sdk_appflow.types.singular_connector_profile_properties.SingularConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Singular. </p>"""
    slack: NotRequired[
        "aws_sdk_appflow.types.slack_connector_profile_properties.SlackConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Slack. </p>"""
    snowflake: NotRequired[
        "aws_sdk_appflow.types.snowflake_connector_profile_properties.SnowflakeConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Snowflake. </p>"""
    trendmicro: NotRequired[
        "aws_sdk_appflow.types.trendmicro_connector_profile_properties.TrendmicroConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Trend Micro. </p>"""
    veeva: NotRequired[
        "aws_sdk_appflow.types.veeva_connector_profile_properties.VeevaConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Veeva. </p>"""
    zendesk: NotRequired[
        "aws_sdk_appflow.types.zendesk_connector_profile_properties.ZendeskConnectorProfileProperties"
    ]
    """<p> The connector-specific properties required by Zendesk. </p>"""
    sapo_data: NotRequired[
        "aws_sdk_appflow.types.sapo_data_connector_profile_properties.SAPODataConnectorProfileProperties"
    ]
    custom_connector: NotRequired[
        "aws_sdk_appflow.types.custom_connector_profile_properties.CustomConnectorProfileProperties"
    ]
    """<p>The properties required by the custom connector.</p>"""
    pardot: NotRequired[
        "aws_sdk_appflow.types.pardot_connector_profile_properties.PardotConnectorProfileProperties"
    ]
    """<p>The connector-specific properties required by Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileProperties) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import aws_sdk_appflow.types.amplitude_connector_profile_properties

        out["Amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_profile_properties.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import aws_sdk_appflow.types.datadog_connector_profile_properties

        out["Datadog"] = (
            aws_sdk_appflow.types.datadog_connector_profile_properties.serialize_json(
                value["datadog"]
            )
        )
    if "dynatrace" in value:
        import aws_sdk_appflow.types.dynatrace_connector_profile_properties

        out["Dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_profile_properties.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import aws_sdk_appflow.types.google_analytics_connector_profile_properties

        out["GoogleAnalytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_profile_properties.serialize_json(
                value["google_analytics"]
            )
        )
    if "honeycode" in value:
        import aws_sdk_appflow.types.honeycode_connector_profile_properties

        out["Honeycode"] = (
            aws_sdk_appflow.types.honeycode_connector_profile_properties.serialize_json(
                value["honeycode"]
            )
        )
    if "infor_nexus" in value:
        import aws_sdk_appflow.types.infor_nexus_connector_profile_properties

        out["InforNexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_profile_properties.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_connector_profile_properties

        out["Marketo"] = (
            aws_sdk_appflow.types.marketo_connector_profile_properties.serialize_json(
                value["marketo"]
            )
        )
    if "redshift" in value:
        import aws_sdk_appflow.types.redshift_connector_profile_properties

        out["Redshift"] = (
            aws_sdk_appflow.types.redshift_connector_profile_properties.serialize_json(
                value["redshift"]
            )
        )
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_connector_profile_properties

        out["Salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_profile_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_appflow.types.service_now_connector_profile_properties

        out["ServiceNow"] = (
            aws_sdk_appflow.types.service_now_connector_profile_properties.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import aws_sdk_appflow.types.singular_connector_profile_properties

        out["Singular"] = (
            aws_sdk_appflow.types.singular_connector_profile_properties.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import aws_sdk_appflow.types.slack_connector_profile_properties

        out["Slack"] = (
            aws_sdk_appflow.types.slack_connector_profile_properties.serialize_json(
                value["slack"]
            )
        )
    if "snowflake" in value:
        import aws_sdk_appflow.types.snowflake_connector_profile_properties

        out["Snowflake"] = (
            aws_sdk_appflow.types.snowflake_connector_profile_properties.serialize_json(
                value["snowflake"]
            )
        )
    if "trendmicro" in value:
        import aws_sdk_appflow.types.trendmicro_connector_profile_properties

        out["Trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_profile_properties.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import aws_sdk_appflow.types.veeva_connector_profile_properties

        out["Veeva"] = (
            aws_sdk_appflow.types.veeva_connector_profile_properties.serialize_json(
                value["veeva"]
            )
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_connector_profile_properties

        out["Zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_profile_properties.serialize_json(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_connector_profile_properties

        out["SAPOData"] = (
            aws_sdk_appflow.types.sapo_data_connector_profile_properties.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import aws_sdk_appflow.types.custom_connector_profile_properties

        out["CustomConnector"] = (
            aws_sdk_appflow.types.custom_connector_profile_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import aws_sdk_appflow.types.pardot_connector_profile_properties

        out["Pardot"] = (
            aws_sdk_appflow.types.pardot_connector_profile_properties.serialize_json(
                value["pardot"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileProperties:
    out: ConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import aws_sdk_appflow.types.amplitude_connector_profile_properties

        out["amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_profile_properties.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import aws_sdk_appflow.types.datadog_connector_profile_properties

        out["datadog"] = (
            aws_sdk_appflow.types.datadog_connector_profile_properties.deserialize_json(
                data["Datadog"]
            )
        )
    if "Dynatrace" in data:
        import aws_sdk_appflow.types.dynatrace_connector_profile_properties

        out["dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_profile_properties.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import aws_sdk_appflow.types.google_analytics_connector_profile_properties

        out["google_analytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_profile_properties.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "Honeycode" in data:
        import aws_sdk_appflow.types.honeycode_connector_profile_properties

        out["honeycode"] = (
            aws_sdk_appflow.types.honeycode_connector_profile_properties.deserialize_json(
                data["Honeycode"]
            )
        )
    if "InforNexus" in data:
        import aws_sdk_appflow.types.infor_nexus_connector_profile_properties

        out["infor_nexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_profile_properties.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_connector_profile_properties

        out["marketo"] = (
            aws_sdk_appflow.types.marketo_connector_profile_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "Redshift" in data:
        import aws_sdk_appflow.types.redshift_connector_profile_properties

        out["redshift"] = (
            aws_sdk_appflow.types.redshift_connector_profile_properties.deserialize_json(
                data["Redshift"]
            )
        )
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_connector_profile_properties

        out["salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_profile_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_appflow.types.service_now_connector_profile_properties

        out["service_now"] = (
            aws_sdk_appflow.types.service_now_connector_profile_properties.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import aws_sdk_appflow.types.singular_connector_profile_properties

        out["singular"] = (
            aws_sdk_appflow.types.singular_connector_profile_properties.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import aws_sdk_appflow.types.slack_connector_profile_properties

        out["slack"] = (
            aws_sdk_appflow.types.slack_connector_profile_properties.deserialize_json(
                data["Slack"]
            )
        )
    if "Snowflake" in data:
        import aws_sdk_appflow.types.snowflake_connector_profile_properties

        out["snowflake"] = (
            aws_sdk_appflow.types.snowflake_connector_profile_properties.deserialize_json(
                data["Snowflake"]
            )
        )
    if "Trendmicro" in data:
        import aws_sdk_appflow.types.trendmicro_connector_profile_properties

        out["trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_profile_properties.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import aws_sdk_appflow.types.veeva_connector_profile_properties

        out["veeva"] = (
            aws_sdk_appflow.types.veeva_connector_profile_properties.deserialize_json(
                data["Veeva"]
            )
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_connector_profile_properties

        out["zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_profile_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_connector_profile_properties

        out["sapo_data"] = (
            aws_sdk_appflow.types.sapo_data_connector_profile_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import aws_sdk_appflow.types.custom_connector_profile_properties

        out["custom_connector"] = (
            aws_sdk_appflow.types.custom_connector_profile_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "Pardot" in data:
        import aws_sdk_appflow.types.pardot_connector_profile_properties

        out["pardot"] = (
            aws_sdk_appflow.types.pardot_connector_profile_properties.deserialize_json(
                data["Pardot"]
            )
        )
    return out
