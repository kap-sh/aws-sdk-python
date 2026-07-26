"""Generated from Smithy shape ``com.amazonaws.appflow#SourceConnectorProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.amplitude_source_properties
    import capo_appflow.types.custom_connector_source_properties
    import capo_appflow.types.datadog_source_properties
    import capo_appflow.types.dynatrace_source_properties
    import capo_appflow.types.google_analytics_source_properties
    import capo_appflow.types.infor_nexus_source_properties
    import capo_appflow.types.marketo_source_properties
    import capo_appflow.types.pardot_source_properties
    import capo_appflow.types.s3_source_properties
    import capo_appflow.types.salesforce_source_properties
    import capo_appflow.types.sapo_data_source_properties
    import capo_appflow.types.service_now_source_properties
    import capo_appflow.types.singular_source_properties
    import capo_appflow.types.slack_source_properties
    import capo_appflow.types.trendmicro_source_properties
    import capo_appflow.types.veeva_source_properties
    import capo_appflow.types.zendesk_source_properties


class SourceConnectorProperties(TypedDict, closed=True):
    amplitude: NotRequired[
        "capo_appflow.types.amplitude_source_properties.AmplitudeSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Amplitude. </p>"""
    datadog: NotRequired[
        "capo_appflow.types.datadog_source_properties.DatadogSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Datadog. </p>"""
    dynatrace: NotRequired[
        "capo_appflow.types.dynatrace_source_properties.DynatraceSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Dynatrace. </p>"""
    google_analytics: NotRequired[
        "capo_appflow.types.google_analytics_source_properties.GoogleAnalyticsSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Google Analytics. </p>"""
    infor_nexus: NotRequired[
        "capo_appflow.types.infor_nexus_source_properties.InforNexusSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Infor Nexus. </p>"""
    marketo: NotRequired[
        "capo_appflow.types.marketo_source_properties.MarketoSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Marketo. </p>"""
    s3: NotRequired["capo_appflow.types.s3_source_properties.S3SourceProperties"]
    """<p> Specifies the information that is required for querying Amazon S3. </p>"""
    salesforce: NotRequired[
        "capo_appflow.types.salesforce_source_properties.SalesforceSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Salesforce. </p>"""
    service_now: NotRequired[
        "capo_appflow.types.service_now_source_properties.ServiceNowSourceProperties"
    ]
    """<p> Specifies the information that is required for querying ServiceNow. </p>"""
    singular: NotRequired[
        "capo_appflow.types.singular_source_properties.SingularSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Singular. </p>"""
    slack: NotRequired[
        "capo_appflow.types.slack_source_properties.SlackSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Slack. </p>"""
    trendmicro: NotRequired[
        "capo_appflow.types.trendmicro_source_properties.TrendmicroSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Trend Micro. </p>"""
    veeva: NotRequired[
        "capo_appflow.types.veeva_source_properties.VeevaSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Veeva. </p>"""
    zendesk: NotRequired[
        "capo_appflow.types.zendesk_source_properties.ZendeskSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Zendesk. </p>"""
    sapo_data: NotRequired[
        "capo_appflow.types.sapo_data_source_properties.SAPODataSourceProperties"
    ]
    custom_connector: NotRequired[
        "capo_appflow.types.custom_connector_source_properties.CustomConnectorSourceProperties"
    ]
    pardot: NotRequired[
        "capo_appflow.types.pardot_source_properties.PardotSourceProperties"
    ]
    """<p>Specifies the information that is required for querying Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConnectorProperties) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import capo_appflow.types.amplitude_source_properties

        out["Amplitude"] = (
            capo_appflow.types.amplitude_source_properties.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import capo_appflow.types.datadog_source_properties

        out["Datadog"] = capo_appflow.types.datadog_source_properties.serialize_json(
            value["datadog"]
        )
    if "dynatrace" in value:
        import capo_appflow.types.dynatrace_source_properties

        out["Dynatrace"] = (
            capo_appflow.types.dynatrace_source_properties.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import capo_appflow.types.google_analytics_source_properties

        out["GoogleAnalytics"] = (
            capo_appflow.types.google_analytics_source_properties.serialize_json(
                value["google_analytics"]
            )
        )
    if "infor_nexus" in value:
        import capo_appflow.types.infor_nexus_source_properties

        out["InforNexus"] = (
            capo_appflow.types.infor_nexus_source_properties.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_source_properties

        out["Marketo"] = capo_appflow.types.marketo_source_properties.serialize_json(
            value["marketo"]
        )
    if "s3" in value:
        import capo_appflow.types.s3_source_properties

        out["S3"] = capo_appflow.types.s3_source_properties.serialize_json(value["s3"])
    if "salesforce" in value:
        import capo_appflow.types.salesforce_source_properties

        out["Salesforce"] = (
            capo_appflow.types.salesforce_source_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import capo_appflow.types.service_now_source_properties

        out["ServiceNow"] = (
            capo_appflow.types.service_now_source_properties.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import capo_appflow.types.singular_source_properties

        out["Singular"] = capo_appflow.types.singular_source_properties.serialize_json(
            value["singular"]
        )
    if "slack" in value:
        import capo_appflow.types.slack_source_properties

        out["Slack"] = capo_appflow.types.slack_source_properties.serialize_json(
            value["slack"]
        )
    if "trendmicro" in value:
        import capo_appflow.types.trendmicro_source_properties

        out["Trendmicro"] = (
            capo_appflow.types.trendmicro_source_properties.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import capo_appflow.types.veeva_source_properties

        out["Veeva"] = capo_appflow.types.veeva_source_properties.serialize_json(
            value["veeva"]
        )
    if "zendesk" in value:
        import capo_appflow.types.zendesk_source_properties

        out["Zendesk"] = capo_appflow.types.zendesk_source_properties.serialize_json(
            value["zendesk"]
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_source_properties

        out["SAPOData"] = capo_appflow.types.sapo_data_source_properties.serialize_json(
            value["sapo_data"]
        )
    if "custom_connector" in value:
        import capo_appflow.types.custom_connector_source_properties

        out["CustomConnector"] = (
            capo_appflow.types.custom_connector_source_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import capo_appflow.types.pardot_source_properties

        out["Pardot"] = capo_appflow.types.pardot_source_properties.serialize_json(
            value["pardot"]
        )
    return out


def deserialize_json(data: dict) -> SourceConnectorProperties:
    out: SourceConnectorProperties = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import capo_appflow.types.amplitude_source_properties

        out["amplitude"] = (
            capo_appflow.types.amplitude_source_properties.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import capo_appflow.types.datadog_source_properties

        out["datadog"] = capo_appflow.types.datadog_source_properties.deserialize_json(
            data["Datadog"]
        )
    if "Dynatrace" in data:
        import capo_appflow.types.dynatrace_source_properties

        out["dynatrace"] = (
            capo_appflow.types.dynatrace_source_properties.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import capo_appflow.types.google_analytics_source_properties

        out["google_analytics"] = (
            capo_appflow.types.google_analytics_source_properties.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "InforNexus" in data:
        import capo_appflow.types.infor_nexus_source_properties

        out["infor_nexus"] = (
            capo_appflow.types.infor_nexus_source_properties.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import capo_appflow.types.marketo_source_properties

        out["marketo"] = capo_appflow.types.marketo_source_properties.deserialize_json(
            data["Marketo"]
        )
    if "S3" in data:
        import capo_appflow.types.s3_source_properties

        out["s3"] = capo_appflow.types.s3_source_properties.deserialize_json(data["S3"])
    if "Salesforce" in data:
        import capo_appflow.types.salesforce_source_properties

        out["salesforce"] = (
            capo_appflow.types.salesforce_source_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import capo_appflow.types.service_now_source_properties

        out["service_now"] = (
            capo_appflow.types.service_now_source_properties.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import capo_appflow.types.singular_source_properties

        out["singular"] = (
            capo_appflow.types.singular_source_properties.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import capo_appflow.types.slack_source_properties

        out["slack"] = capo_appflow.types.slack_source_properties.deserialize_json(
            data["Slack"]
        )
    if "Trendmicro" in data:
        import capo_appflow.types.trendmicro_source_properties

        out["trendmicro"] = (
            capo_appflow.types.trendmicro_source_properties.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import capo_appflow.types.veeva_source_properties

        out["veeva"] = capo_appflow.types.veeva_source_properties.deserialize_json(
            data["Veeva"]
        )
    if "Zendesk" in data:
        import capo_appflow.types.zendesk_source_properties

        out["zendesk"] = capo_appflow.types.zendesk_source_properties.deserialize_json(
            data["Zendesk"]
        )
    if "SAPOData" in data:
        import capo_appflow.types.sapo_data_source_properties

        out["sapo_data"] = (
            capo_appflow.types.sapo_data_source_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import capo_appflow.types.custom_connector_source_properties

        out["custom_connector"] = (
            capo_appflow.types.custom_connector_source_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "Pardot" in data:
        import capo_appflow.types.pardot_source_properties

        out["pardot"] = capo_appflow.types.pardot_source_properties.deserialize_json(
            data["Pardot"]
        )
    return out
