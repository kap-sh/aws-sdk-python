"""Generated from Smithy shape ``com.amazonaws.appflow#SourceConnectorProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.amplitude_source_properties
    import aws_sdk_appflow.types.custom_connector_source_properties
    import aws_sdk_appflow.types.datadog_source_properties
    import aws_sdk_appflow.types.dynatrace_source_properties
    import aws_sdk_appflow.types.google_analytics_source_properties
    import aws_sdk_appflow.types.infor_nexus_source_properties
    import aws_sdk_appflow.types.marketo_source_properties
    import aws_sdk_appflow.types.pardot_source_properties
    import aws_sdk_appflow.types.s3_source_properties
    import aws_sdk_appflow.types.salesforce_source_properties
    import aws_sdk_appflow.types.sapo_data_source_properties
    import aws_sdk_appflow.types.service_now_source_properties
    import aws_sdk_appflow.types.singular_source_properties
    import aws_sdk_appflow.types.slack_source_properties
    import aws_sdk_appflow.types.trendmicro_source_properties
    import aws_sdk_appflow.types.veeva_source_properties
    import aws_sdk_appflow.types.zendesk_source_properties


class SourceConnectorProperties(TypedDict, closed=True):
    amplitude: NotRequired[
        "aws_sdk_appflow.types.amplitude_source_properties.AmplitudeSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Amplitude. </p>"""
    datadog: NotRequired[
        "aws_sdk_appflow.types.datadog_source_properties.DatadogSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Datadog. </p>"""
    dynatrace: NotRequired[
        "aws_sdk_appflow.types.dynatrace_source_properties.DynatraceSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Dynatrace. </p>"""
    google_analytics: NotRequired[
        "aws_sdk_appflow.types.google_analytics_source_properties.GoogleAnalyticsSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Google Analytics. </p>"""
    infor_nexus: NotRequired[
        "aws_sdk_appflow.types.infor_nexus_source_properties.InforNexusSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Infor Nexus. </p>"""
    marketo: NotRequired[
        "aws_sdk_appflow.types.marketo_source_properties.MarketoSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Marketo. </p>"""
    s3: NotRequired["aws_sdk_appflow.types.s3_source_properties.S3SourceProperties"]
    """<p> Specifies the information that is required for querying Amazon S3. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_source_properties.SalesforceSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Salesforce. </p>"""
    service_now: NotRequired[
        "aws_sdk_appflow.types.service_now_source_properties.ServiceNowSourceProperties"
    ]
    """<p> Specifies the information that is required for querying ServiceNow. </p>"""
    singular: NotRequired[
        "aws_sdk_appflow.types.singular_source_properties.SingularSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Singular. </p>"""
    slack: NotRequired[
        "aws_sdk_appflow.types.slack_source_properties.SlackSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Slack. </p>"""
    trendmicro: NotRequired[
        "aws_sdk_appflow.types.trendmicro_source_properties.TrendmicroSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Trend Micro. </p>"""
    veeva: NotRequired[
        "aws_sdk_appflow.types.veeva_source_properties.VeevaSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Veeva. </p>"""
    zendesk: NotRequired[
        "aws_sdk_appflow.types.zendesk_source_properties.ZendeskSourceProperties"
    ]
    """<p> Specifies the information that is required for querying Zendesk. </p>"""
    sapo_data: NotRequired[
        "aws_sdk_appflow.types.sapo_data_source_properties.SAPODataSourceProperties"
    ]
    custom_connector: NotRequired[
        "aws_sdk_appflow.types.custom_connector_source_properties.CustomConnectorSourceProperties"
    ]
    pardot: NotRequired[
        "aws_sdk_appflow.types.pardot_source_properties.PardotSourceProperties"
    ]
    """<p>Specifies the information that is required for querying Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConnectorProperties) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import aws_sdk_appflow.types.amplitude_source_properties

        out["Amplitude"] = (
            aws_sdk_appflow.types.amplitude_source_properties.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import aws_sdk_appflow.types.datadog_source_properties

        out["Datadog"] = aws_sdk_appflow.types.datadog_source_properties.serialize_json(
            value["datadog"]
        )
    if "dynatrace" in value:
        import aws_sdk_appflow.types.dynatrace_source_properties

        out["Dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_source_properties.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import aws_sdk_appflow.types.google_analytics_source_properties

        out["GoogleAnalytics"] = (
            aws_sdk_appflow.types.google_analytics_source_properties.serialize_json(
                value["google_analytics"]
            )
        )
    if "infor_nexus" in value:
        import aws_sdk_appflow.types.infor_nexus_source_properties

        out["InforNexus"] = (
            aws_sdk_appflow.types.infor_nexus_source_properties.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_source_properties

        out["Marketo"] = aws_sdk_appflow.types.marketo_source_properties.serialize_json(
            value["marketo"]
        )
    if "s3" in value:
        import aws_sdk_appflow.types.s3_source_properties

        out["S3"] = aws_sdk_appflow.types.s3_source_properties.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_source_properties

        out["Salesforce"] = (
            aws_sdk_appflow.types.salesforce_source_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_appflow.types.service_now_source_properties

        out["ServiceNow"] = (
            aws_sdk_appflow.types.service_now_source_properties.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import aws_sdk_appflow.types.singular_source_properties

        out["Singular"] = (
            aws_sdk_appflow.types.singular_source_properties.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import aws_sdk_appflow.types.slack_source_properties

        out["Slack"] = aws_sdk_appflow.types.slack_source_properties.serialize_json(
            value["slack"]
        )
    if "trendmicro" in value:
        import aws_sdk_appflow.types.trendmicro_source_properties

        out["Trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_source_properties.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import aws_sdk_appflow.types.veeva_source_properties

        out["Veeva"] = aws_sdk_appflow.types.veeva_source_properties.serialize_json(
            value["veeva"]
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_source_properties

        out["Zendesk"] = aws_sdk_appflow.types.zendesk_source_properties.serialize_json(
            value["zendesk"]
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_source_properties

        out["SAPOData"] = (
            aws_sdk_appflow.types.sapo_data_source_properties.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import aws_sdk_appflow.types.custom_connector_source_properties

        out["CustomConnector"] = (
            aws_sdk_appflow.types.custom_connector_source_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import aws_sdk_appflow.types.pardot_source_properties

        out["Pardot"] = aws_sdk_appflow.types.pardot_source_properties.serialize_json(
            value["pardot"]
        )
    return out


def deserialize_json(data: dict) -> SourceConnectorProperties:
    out: SourceConnectorProperties = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import aws_sdk_appflow.types.amplitude_source_properties

        out["amplitude"] = (
            aws_sdk_appflow.types.amplitude_source_properties.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import aws_sdk_appflow.types.datadog_source_properties

        out["datadog"] = (
            aws_sdk_appflow.types.datadog_source_properties.deserialize_json(
                data["Datadog"]
            )
        )
    if "Dynatrace" in data:
        import aws_sdk_appflow.types.dynatrace_source_properties

        out["dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_source_properties.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import aws_sdk_appflow.types.google_analytics_source_properties

        out["google_analytics"] = (
            aws_sdk_appflow.types.google_analytics_source_properties.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "InforNexus" in data:
        import aws_sdk_appflow.types.infor_nexus_source_properties

        out["infor_nexus"] = (
            aws_sdk_appflow.types.infor_nexus_source_properties.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_source_properties

        out["marketo"] = (
            aws_sdk_appflow.types.marketo_source_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "S3" in data:
        import aws_sdk_appflow.types.s3_source_properties

        out["s3"] = aws_sdk_appflow.types.s3_source_properties.deserialize_json(
            data["S3"]
        )
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_source_properties

        out["salesforce"] = (
            aws_sdk_appflow.types.salesforce_source_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_appflow.types.service_now_source_properties

        out["service_now"] = (
            aws_sdk_appflow.types.service_now_source_properties.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import aws_sdk_appflow.types.singular_source_properties

        out["singular"] = (
            aws_sdk_appflow.types.singular_source_properties.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import aws_sdk_appflow.types.slack_source_properties

        out["slack"] = aws_sdk_appflow.types.slack_source_properties.deserialize_json(
            data["Slack"]
        )
    if "Trendmicro" in data:
        import aws_sdk_appflow.types.trendmicro_source_properties

        out["trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_source_properties.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import aws_sdk_appflow.types.veeva_source_properties

        out["veeva"] = aws_sdk_appflow.types.veeva_source_properties.deserialize_json(
            data["Veeva"]
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_source_properties

        out["zendesk"] = (
            aws_sdk_appflow.types.zendesk_source_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_source_properties

        out["sapo_data"] = (
            aws_sdk_appflow.types.sapo_data_source_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import aws_sdk_appflow.types.custom_connector_source_properties

        out["custom_connector"] = (
            aws_sdk_appflow.types.custom_connector_source_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "Pardot" in data:
        import aws_sdk_appflow.types.pardot_source_properties

        out["pardot"] = aws_sdk_appflow.types.pardot_source_properties.deserialize_json(
            data["Pardot"]
        )
    return out
