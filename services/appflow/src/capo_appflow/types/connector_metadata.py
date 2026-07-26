"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.amplitude_metadata
    import capo_appflow.types.customer_profiles_metadata
    import capo_appflow.types.datadog_metadata
    import capo_appflow.types.dynatrace_metadata
    import capo_appflow.types.event_bridge_metadata
    import capo_appflow.types.google_analytics_metadata
    import capo_appflow.types.honeycode_metadata
    import capo_appflow.types.infor_nexus_metadata
    import capo_appflow.types.marketo_metadata
    import capo_appflow.types.pardot_metadata
    import capo_appflow.types.redshift_metadata
    import capo_appflow.types.s3_metadata
    import capo_appflow.types.salesforce_metadata
    import capo_appflow.types.sapo_data_metadata
    import capo_appflow.types.service_now_metadata
    import capo_appflow.types.singular_metadata
    import capo_appflow.types.slack_metadata
    import capo_appflow.types.snowflake_metadata
    import capo_appflow.types.trendmicro_metadata
    import capo_appflow.types.upsolver_metadata
    import capo_appflow.types.veeva_metadata
    import capo_appflow.types.zendesk_metadata


class ConnectorMetadata(TypedDict, closed=True):
    amplitude: NotRequired["capo_appflow.types.amplitude_metadata.AmplitudeMetadata"]
    """<p> The connector metadata specific to Amplitude. </p>"""
    datadog: NotRequired["capo_appflow.types.datadog_metadata.DatadogMetadata"]
    """<p> The connector metadata specific to Datadog. </p>"""
    dynatrace: NotRequired["capo_appflow.types.dynatrace_metadata.DynatraceMetadata"]
    """<p> The connector metadata specific to Dynatrace. </p>"""
    google_analytics: NotRequired[
        "capo_appflow.types.google_analytics_metadata.GoogleAnalyticsMetadata"
    ]
    """<p> The connector metadata specific to Google Analytics. </p>"""
    infor_nexus: NotRequired[
        "capo_appflow.types.infor_nexus_metadata.InforNexusMetadata"
    ]
    """<p> The connector metadata specific to Infor Nexus. </p>"""
    marketo: NotRequired["capo_appflow.types.marketo_metadata.MarketoMetadata"]
    """<p> The connector metadata specific to Marketo. </p>"""
    redshift: NotRequired["capo_appflow.types.redshift_metadata.RedshiftMetadata"]
    """<p> The connector metadata specific to Amazon Redshift. </p>"""
    s3: NotRequired["capo_appflow.types.s3_metadata.S3Metadata"]
    """<p> The connector metadata specific to Amazon S3. </p>"""
    salesforce: NotRequired["capo_appflow.types.salesforce_metadata.SalesforceMetadata"]
    """<p> The connector metadata specific to Salesforce. </p>"""
    service_now: NotRequired[
        "capo_appflow.types.service_now_metadata.ServiceNowMetadata"
    ]
    """<p> The connector metadata specific to ServiceNow. </p>"""
    singular: NotRequired["capo_appflow.types.singular_metadata.SingularMetadata"]
    """<p> The connector metadata specific to Singular. </p>"""
    slack: NotRequired["capo_appflow.types.slack_metadata.SlackMetadata"]
    """<p> The connector metadata specific to Slack. </p>"""
    snowflake: NotRequired["capo_appflow.types.snowflake_metadata.SnowflakeMetadata"]
    """<p> The connector metadata specific to Snowflake. </p>"""
    trendmicro: NotRequired["capo_appflow.types.trendmicro_metadata.TrendmicroMetadata"]
    """<p> The connector metadata specific to Trend Micro. </p>"""
    veeva: NotRequired["capo_appflow.types.veeva_metadata.VeevaMetadata"]
    """<p> The connector metadata specific to Veeva. </p>"""
    zendesk: NotRequired["capo_appflow.types.zendesk_metadata.ZendeskMetadata"]
    """<p> The connector metadata specific to Zendesk. </p>"""
    event_bridge: NotRequired[
        "capo_appflow.types.event_bridge_metadata.EventBridgeMetadata"
    ]
    """<p> The connector metadata specific to Amazon EventBridge. </p>"""
    upsolver: NotRequired["capo_appflow.types.upsolver_metadata.UpsolverMetadata"]
    """<p> The connector metadata specific to Upsolver. </p>"""
    customer_profiles: NotRequired[
        "capo_appflow.types.customer_profiles_metadata.CustomerProfilesMetadata"
    ]
    """<p> The connector metadata specific to Connect Customer Customer Profiles. </p>"""
    honeycode: NotRequired["capo_appflow.types.honeycode_metadata.HoneycodeMetadata"]
    """<p> The connector metadata specific to Amazon Honeycode. </p>"""
    sapo_data: NotRequired["capo_appflow.types.sapo_data_metadata.SAPODataMetadata"]
    pardot: NotRequired["capo_appflow.types.pardot_metadata.PardotMetadata"]
    """<p>The connector metadata specific to Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorMetadata) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import capo_appflow.types.amplitude_metadata

        out["Amplitude"] = capo_appflow.types.amplitude_metadata.serialize_json(
            value["amplitude"]
        )
    if "datadog" in value:
        import capo_appflow.types.datadog_metadata

        out["Datadog"] = capo_appflow.types.datadog_metadata.serialize_json(
            value["datadog"]
        )
    if "dynatrace" in value:
        import capo_appflow.types.dynatrace_metadata

        out["Dynatrace"] = capo_appflow.types.dynatrace_metadata.serialize_json(
            value["dynatrace"]
        )
    if "google_analytics" in value:
        import capo_appflow.types.google_analytics_metadata

        out["GoogleAnalytics"] = (
            capo_appflow.types.google_analytics_metadata.serialize_json(
                value["google_analytics"]
            )
        )
    if "infor_nexus" in value:
        import capo_appflow.types.infor_nexus_metadata

        out["InforNexus"] = capo_appflow.types.infor_nexus_metadata.serialize_json(
            value["infor_nexus"]
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_metadata

        out["Marketo"] = capo_appflow.types.marketo_metadata.serialize_json(
            value["marketo"]
        )
    if "redshift" in value:
        import capo_appflow.types.redshift_metadata

        out["Redshift"] = capo_appflow.types.redshift_metadata.serialize_json(
            value["redshift"]
        )
    if "s3" in value:
        import capo_appflow.types.s3_metadata

        out["S3"] = capo_appflow.types.s3_metadata.serialize_json(value["s3"])
    if "salesforce" in value:
        import capo_appflow.types.salesforce_metadata

        out["Salesforce"] = capo_appflow.types.salesforce_metadata.serialize_json(
            value["salesforce"]
        )
    if "service_now" in value:
        import capo_appflow.types.service_now_metadata

        out["ServiceNow"] = capo_appflow.types.service_now_metadata.serialize_json(
            value["service_now"]
        )
    if "singular" in value:
        import capo_appflow.types.singular_metadata

        out["Singular"] = capo_appflow.types.singular_metadata.serialize_json(
            value["singular"]
        )
    if "slack" in value:
        import capo_appflow.types.slack_metadata

        out["Slack"] = capo_appflow.types.slack_metadata.serialize_json(value["slack"])
    if "snowflake" in value:
        import capo_appflow.types.snowflake_metadata

        out["Snowflake"] = capo_appflow.types.snowflake_metadata.serialize_json(
            value["snowflake"]
        )
    if "trendmicro" in value:
        import capo_appflow.types.trendmicro_metadata

        out["Trendmicro"] = capo_appflow.types.trendmicro_metadata.serialize_json(
            value["trendmicro"]
        )
    if "veeva" in value:
        import capo_appflow.types.veeva_metadata

        out["Veeva"] = capo_appflow.types.veeva_metadata.serialize_json(value["veeva"])
    if "zendesk" in value:
        import capo_appflow.types.zendesk_metadata

        out["Zendesk"] = capo_appflow.types.zendesk_metadata.serialize_json(
            value["zendesk"]
        )
    if "event_bridge" in value:
        import capo_appflow.types.event_bridge_metadata

        out["EventBridge"] = capo_appflow.types.event_bridge_metadata.serialize_json(
            value["event_bridge"]
        )
    if "upsolver" in value:
        import capo_appflow.types.upsolver_metadata

        out["Upsolver"] = capo_appflow.types.upsolver_metadata.serialize_json(
            value["upsolver"]
        )
    if "customer_profiles" in value:
        import capo_appflow.types.customer_profiles_metadata

        out["CustomerProfiles"] = (
            capo_appflow.types.customer_profiles_metadata.serialize_json(
                value["customer_profiles"]
            )
        )
    if "honeycode" in value:
        import capo_appflow.types.honeycode_metadata

        out["Honeycode"] = capo_appflow.types.honeycode_metadata.serialize_json(
            value["honeycode"]
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_metadata

        out["SAPOData"] = capo_appflow.types.sapo_data_metadata.serialize_json(
            value["sapo_data"]
        )
    if "pardot" in value:
        import capo_appflow.types.pardot_metadata

        out["Pardot"] = capo_appflow.types.pardot_metadata.serialize_json(
            value["pardot"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorMetadata:
    out: ConnectorMetadata = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import capo_appflow.types.amplitude_metadata

        out["amplitude"] = capo_appflow.types.amplitude_metadata.deserialize_json(
            data["Amplitude"]
        )
    if "Datadog" in data:
        import capo_appflow.types.datadog_metadata

        out["datadog"] = capo_appflow.types.datadog_metadata.deserialize_json(
            data["Datadog"]
        )
    if "Dynatrace" in data:
        import capo_appflow.types.dynatrace_metadata

        out["dynatrace"] = capo_appflow.types.dynatrace_metadata.deserialize_json(
            data["Dynatrace"]
        )
    if "GoogleAnalytics" in data:
        import capo_appflow.types.google_analytics_metadata

        out["google_analytics"] = (
            capo_appflow.types.google_analytics_metadata.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "InforNexus" in data:
        import capo_appflow.types.infor_nexus_metadata

        out["infor_nexus"] = capo_appflow.types.infor_nexus_metadata.deserialize_json(
            data["InforNexus"]
        )
    if "Marketo" in data:
        import capo_appflow.types.marketo_metadata

        out["marketo"] = capo_appflow.types.marketo_metadata.deserialize_json(
            data["Marketo"]
        )
    if "Redshift" in data:
        import capo_appflow.types.redshift_metadata

        out["redshift"] = capo_appflow.types.redshift_metadata.deserialize_json(
            data["Redshift"]
        )
    if "S3" in data:
        import capo_appflow.types.s3_metadata

        out["s3"] = capo_appflow.types.s3_metadata.deserialize_json(data["S3"])
    if "Salesforce" in data:
        import capo_appflow.types.salesforce_metadata

        out["salesforce"] = capo_appflow.types.salesforce_metadata.deserialize_json(
            data["Salesforce"]
        )
    if "ServiceNow" in data:
        import capo_appflow.types.service_now_metadata

        out["service_now"] = capo_appflow.types.service_now_metadata.deserialize_json(
            data["ServiceNow"]
        )
    if "Singular" in data:
        import capo_appflow.types.singular_metadata

        out["singular"] = capo_appflow.types.singular_metadata.deserialize_json(
            data["Singular"]
        )
    if "Slack" in data:
        import capo_appflow.types.slack_metadata

        out["slack"] = capo_appflow.types.slack_metadata.deserialize_json(data["Slack"])
    if "Snowflake" in data:
        import capo_appflow.types.snowflake_metadata

        out["snowflake"] = capo_appflow.types.snowflake_metadata.deserialize_json(
            data["Snowflake"]
        )
    if "Trendmicro" in data:
        import capo_appflow.types.trendmicro_metadata

        out["trendmicro"] = capo_appflow.types.trendmicro_metadata.deserialize_json(
            data["Trendmicro"]
        )
    if "Veeva" in data:
        import capo_appflow.types.veeva_metadata

        out["veeva"] = capo_appflow.types.veeva_metadata.deserialize_json(data["Veeva"])
    if "Zendesk" in data:
        import capo_appflow.types.zendesk_metadata

        out["zendesk"] = capo_appflow.types.zendesk_metadata.deserialize_json(
            data["Zendesk"]
        )
    if "EventBridge" in data:
        import capo_appflow.types.event_bridge_metadata

        out["event_bridge"] = capo_appflow.types.event_bridge_metadata.deserialize_json(
            data["EventBridge"]
        )
    if "Upsolver" in data:
        import capo_appflow.types.upsolver_metadata

        out["upsolver"] = capo_appflow.types.upsolver_metadata.deserialize_json(
            data["Upsolver"]
        )
    if "CustomerProfiles" in data:
        import capo_appflow.types.customer_profiles_metadata

        out["customer_profiles"] = (
            capo_appflow.types.customer_profiles_metadata.deserialize_json(
                data["CustomerProfiles"]
            )
        )
    if "Honeycode" in data:
        import capo_appflow.types.honeycode_metadata

        out["honeycode"] = capo_appflow.types.honeycode_metadata.deserialize_json(
            data["Honeycode"]
        )
    if "SAPOData" in data:
        import capo_appflow.types.sapo_data_metadata

        out["sapo_data"] = capo_appflow.types.sapo_data_metadata.deserialize_json(
            data["SAPOData"]
        )
    if "Pardot" in data:
        import capo_appflow.types.pardot_metadata

        out["pardot"] = capo_appflow.types.pardot_metadata.deserialize_json(
            data["Pardot"]
        )
    return out
