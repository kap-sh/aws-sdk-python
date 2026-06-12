"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.amplitude_connector_profile_credentials
    import aws_sdk_appflow.types.custom_connector_profile_credentials
    import aws_sdk_appflow.types.datadog_connector_profile_credentials
    import aws_sdk_appflow.types.dynatrace_connector_profile_credentials
    import aws_sdk_appflow.types.google_analytics_connector_profile_credentials
    import aws_sdk_appflow.types.honeycode_connector_profile_credentials
    import aws_sdk_appflow.types.infor_nexus_connector_profile_credentials
    import aws_sdk_appflow.types.marketo_connector_profile_credentials
    import aws_sdk_appflow.types.pardot_connector_profile_credentials
    import aws_sdk_appflow.types.redshift_connector_profile_credentials
    import aws_sdk_appflow.types.salesforce_connector_profile_credentials
    import aws_sdk_appflow.types.sapo_data_connector_profile_credentials
    import aws_sdk_appflow.types.service_now_connector_profile_credentials
    import aws_sdk_appflow.types.singular_connector_profile_credentials
    import aws_sdk_appflow.types.slack_connector_profile_credentials
    import aws_sdk_appflow.types.snowflake_connector_profile_credentials
    import aws_sdk_appflow.types.trendmicro_connector_profile_credentials
    import aws_sdk_appflow.types.veeva_connector_profile_credentials
    import aws_sdk_appflow.types.zendesk_connector_profile_credentials


class ConnectorProfileCredentials(TypedDict):
    amplitude: NotRequired[
        "aws_sdk_appflow.types.amplitude_connector_profile_credentials.AmplitudeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amplitude. </p>"""
    datadog: NotRequired[
        "aws_sdk_appflow.types.datadog_connector_profile_credentials.DatadogConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Datadog. </p>"""
    dynatrace: NotRequired[
        "aws_sdk_appflow.types.dynatrace_connector_profile_credentials.DynatraceConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Dynatrace. </p>"""
    google_analytics: NotRequired[
        "aws_sdk_appflow.types.google_analytics_connector_profile_credentials.GoogleAnalyticsConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Google Analytics. </p>"""
    honeycode: NotRequired[
        "aws_sdk_appflow.types.honeycode_connector_profile_credentials.HoneycodeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amazon Honeycode. </p>"""
    infor_nexus: NotRequired[
        "aws_sdk_appflow.types.infor_nexus_connector_profile_credentials.InforNexusConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Infor Nexus. </p>"""
    marketo: NotRequired[
        "aws_sdk_appflow.types.marketo_connector_profile_credentials.MarketoConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Marketo. </p>"""
    redshift: NotRequired[
        "aws_sdk_appflow.types.redshift_connector_profile_credentials.RedshiftConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amazon Redshift. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_connector_profile_credentials.SalesforceConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Salesforce. </p>"""
    service_now: NotRequired[
        "aws_sdk_appflow.types.service_now_connector_profile_credentials.ServiceNowConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using ServiceNow. </p>"""
    singular: NotRequired[
        "aws_sdk_appflow.types.singular_connector_profile_credentials.SingularConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Singular. </p>"""
    slack: NotRequired[
        "aws_sdk_appflow.types.slack_connector_profile_credentials.SlackConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Slack. </p>"""
    snowflake: NotRequired[
        "aws_sdk_appflow.types.snowflake_connector_profile_credentials.SnowflakeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Snowflake. </p>"""
    trendmicro: NotRequired[
        "aws_sdk_appflow.types.trendmicro_connector_profile_credentials.TrendmicroConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Trend Micro. </p>"""
    veeva: NotRequired[
        "aws_sdk_appflow.types.veeva_connector_profile_credentials.VeevaConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Veeva. </p>"""
    zendesk: NotRequired[
        "aws_sdk_appflow.types.zendesk_connector_profile_credentials.ZendeskConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Zendesk. </p>"""
    sapo_data: NotRequired[
        "aws_sdk_appflow.types.sapo_data_connector_profile_credentials.SAPODataConnectorProfileCredentials"
    ]
    custom_connector: NotRequired[
        "aws_sdk_appflow.types.custom_connector_profile_credentials.CustomConnectorProfileCredentials"
    ]
    pardot: NotRequired[
        "aws_sdk_appflow.types.pardot_connector_profile_credentials.PardotConnectorProfileCredentials"
    ]
    """<p>The connector-specific credentials required when using Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import aws_sdk_appflow.types.amplitude_connector_profile_credentials

        out["Amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_profile_credentials.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import aws_sdk_appflow.types.datadog_connector_profile_credentials

        out["Datadog"] = (
            aws_sdk_appflow.types.datadog_connector_profile_credentials.serialize_json(
                value["datadog"]
            )
        )
    if "dynatrace" in value:
        import aws_sdk_appflow.types.dynatrace_connector_profile_credentials

        out["Dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_profile_credentials.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import aws_sdk_appflow.types.google_analytics_connector_profile_credentials

        out["GoogleAnalytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_profile_credentials.serialize_json(
                value["google_analytics"]
            )
        )
    if "honeycode" in value:
        import aws_sdk_appflow.types.honeycode_connector_profile_credentials

        out["Honeycode"] = (
            aws_sdk_appflow.types.honeycode_connector_profile_credentials.serialize_json(
                value["honeycode"]
            )
        )
    if "infor_nexus" in value:
        import aws_sdk_appflow.types.infor_nexus_connector_profile_credentials

        out["InforNexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_profile_credentials.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_connector_profile_credentials

        out["Marketo"] = (
            aws_sdk_appflow.types.marketo_connector_profile_credentials.serialize_json(
                value["marketo"]
            )
        )
    if "redshift" in value:
        import aws_sdk_appflow.types.redshift_connector_profile_credentials

        out["Redshift"] = (
            aws_sdk_appflow.types.redshift_connector_profile_credentials.serialize_json(
                value["redshift"]
            )
        )
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_connector_profile_credentials

        out["Salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_profile_credentials.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_appflow.types.service_now_connector_profile_credentials

        out["ServiceNow"] = (
            aws_sdk_appflow.types.service_now_connector_profile_credentials.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import aws_sdk_appflow.types.singular_connector_profile_credentials

        out["Singular"] = (
            aws_sdk_appflow.types.singular_connector_profile_credentials.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import aws_sdk_appflow.types.slack_connector_profile_credentials

        out["Slack"] = (
            aws_sdk_appflow.types.slack_connector_profile_credentials.serialize_json(
                value["slack"]
            )
        )
    if "snowflake" in value:
        import aws_sdk_appflow.types.snowflake_connector_profile_credentials

        out["Snowflake"] = (
            aws_sdk_appflow.types.snowflake_connector_profile_credentials.serialize_json(
                value["snowflake"]
            )
        )
    if "trendmicro" in value:
        import aws_sdk_appflow.types.trendmicro_connector_profile_credentials

        out["Trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_profile_credentials.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import aws_sdk_appflow.types.veeva_connector_profile_credentials

        out["Veeva"] = (
            aws_sdk_appflow.types.veeva_connector_profile_credentials.serialize_json(
                value["veeva"]
            )
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_connector_profile_credentials

        out["Zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_profile_credentials.serialize_json(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_connector_profile_credentials

        out["SAPOData"] = (
            aws_sdk_appflow.types.sapo_data_connector_profile_credentials.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import aws_sdk_appflow.types.custom_connector_profile_credentials

        out["CustomConnector"] = (
            aws_sdk_appflow.types.custom_connector_profile_credentials.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import aws_sdk_appflow.types.pardot_connector_profile_credentials

        out["Pardot"] = (
            aws_sdk_appflow.types.pardot_connector_profile_credentials.serialize_json(
                value["pardot"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileCredentials:
    out: ConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import aws_sdk_appflow.types.amplitude_connector_profile_credentials

        out["amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_profile_credentials.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import aws_sdk_appflow.types.datadog_connector_profile_credentials

        out["datadog"] = (
            aws_sdk_appflow.types.datadog_connector_profile_credentials.deserialize_json(
                data["Datadog"]
            )
        )
    if "Dynatrace" in data:
        import aws_sdk_appflow.types.dynatrace_connector_profile_credentials

        out["dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_profile_credentials.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import aws_sdk_appflow.types.google_analytics_connector_profile_credentials

        out["google_analytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_profile_credentials.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "Honeycode" in data:
        import aws_sdk_appflow.types.honeycode_connector_profile_credentials

        out["honeycode"] = (
            aws_sdk_appflow.types.honeycode_connector_profile_credentials.deserialize_json(
                data["Honeycode"]
            )
        )
    if "InforNexus" in data:
        import aws_sdk_appflow.types.infor_nexus_connector_profile_credentials

        out["infor_nexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_profile_credentials.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_connector_profile_credentials

        out["marketo"] = (
            aws_sdk_appflow.types.marketo_connector_profile_credentials.deserialize_json(
                data["Marketo"]
            )
        )
    if "Redshift" in data:
        import aws_sdk_appflow.types.redshift_connector_profile_credentials

        out["redshift"] = (
            aws_sdk_appflow.types.redshift_connector_profile_credentials.deserialize_json(
                data["Redshift"]
            )
        )
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_connector_profile_credentials

        out["salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_profile_credentials.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_appflow.types.service_now_connector_profile_credentials

        out["service_now"] = (
            aws_sdk_appflow.types.service_now_connector_profile_credentials.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import aws_sdk_appflow.types.singular_connector_profile_credentials

        out["singular"] = (
            aws_sdk_appflow.types.singular_connector_profile_credentials.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import aws_sdk_appflow.types.slack_connector_profile_credentials

        out["slack"] = (
            aws_sdk_appflow.types.slack_connector_profile_credentials.deserialize_json(
                data["Slack"]
            )
        )
    if "Snowflake" in data:
        import aws_sdk_appflow.types.snowflake_connector_profile_credentials

        out["snowflake"] = (
            aws_sdk_appflow.types.snowflake_connector_profile_credentials.deserialize_json(
                data["Snowflake"]
            )
        )
    if "Trendmicro" in data:
        import aws_sdk_appflow.types.trendmicro_connector_profile_credentials

        out["trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_profile_credentials.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import aws_sdk_appflow.types.veeva_connector_profile_credentials

        out["veeva"] = (
            aws_sdk_appflow.types.veeva_connector_profile_credentials.deserialize_json(
                data["Veeva"]
            )
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_connector_profile_credentials

        out["zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_profile_credentials.deserialize_json(
                data["Zendesk"]
            )
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_connector_profile_credentials

        out["sapo_data"] = (
            aws_sdk_appflow.types.sapo_data_connector_profile_credentials.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import aws_sdk_appflow.types.custom_connector_profile_credentials

        out["custom_connector"] = (
            aws_sdk_appflow.types.custom_connector_profile_credentials.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "Pardot" in data:
        import aws_sdk_appflow.types.pardot_connector_profile_credentials

        out["pardot"] = (
            aws_sdk_appflow.types.pardot_connector_profile_credentials.deserialize_json(
                data["Pardot"]
            )
        )
    return out
