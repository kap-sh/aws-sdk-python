"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.amplitude_metadata
    import aws_sdk_appflow.types.customer_profiles_metadata
    import aws_sdk_appflow.types.datadog_metadata
    import aws_sdk_appflow.types.dynatrace_metadata
    import aws_sdk_appflow.types.event_bridge_metadata
    import aws_sdk_appflow.types.google_analytics_metadata
    import aws_sdk_appflow.types.honeycode_metadata
    import aws_sdk_appflow.types.infor_nexus_metadata
    import aws_sdk_appflow.types.marketo_metadata
    import aws_sdk_appflow.types.pardot_metadata
    import aws_sdk_appflow.types.redshift_metadata
    import aws_sdk_appflow.types.s3_metadata
    import aws_sdk_appflow.types.salesforce_metadata
    import aws_sdk_appflow.types.sapo_data_metadata
    import aws_sdk_appflow.types.service_now_metadata
    import aws_sdk_appflow.types.singular_metadata
    import aws_sdk_appflow.types.slack_metadata
    import aws_sdk_appflow.types.snowflake_metadata
    import aws_sdk_appflow.types.trendmicro_metadata
    import aws_sdk_appflow.types.upsolver_metadata
    import aws_sdk_appflow.types.veeva_metadata
    import aws_sdk_appflow.types.zendesk_metadata


class ConnectorMetadata(TypedDict, closed=True):
    amplitude: NotRequired["aws_sdk_appflow.types.amplitude_metadata.AmplitudeMetadata"]
    """<p> The connector metadata specific to Amplitude. </p>"""
    datadog: NotRequired["aws_sdk_appflow.types.datadog_metadata.DatadogMetadata"]
    """<p> The connector metadata specific to Datadog. </p>"""
    dynatrace: NotRequired["aws_sdk_appflow.types.dynatrace_metadata.DynatraceMetadata"]
    """<p> The connector metadata specific to Dynatrace. </p>"""
    google_analytics: NotRequired[
        "aws_sdk_appflow.types.google_analytics_metadata.GoogleAnalyticsMetadata"
    ]
    """<p> The connector metadata specific to Google Analytics. </p>"""
    infor_nexus: NotRequired[
        "aws_sdk_appflow.types.infor_nexus_metadata.InforNexusMetadata"
    ]
    """<p> The connector metadata specific to Infor Nexus. </p>"""
    marketo: NotRequired["aws_sdk_appflow.types.marketo_metadata.MarketoMetadata"]
    """<p> The connector metadata specific to Marketo. </p>"""
    redshift: NotRequired["aws_sdk_appflow.types.redshift_metadata.RedshiftMetadata"]
    """<p> The connector metadata specific to Amazon Redshift. </p>"""
    s3: NotRequired["aws_sdk_appflow.types.s3_metadata.S3Metadata"]
    """<p> The connector metadata specific to Amazon S3. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_metadata.SalesforceMetadata"
    ]
    """<p> The connector metadata specific to Salesforce. </p>"""
    service_now: NotRequired[
        "aws_sdk_appflow.types.service_now_metadata.ServiceNowMetadata"
    ]
    """<p> The connector metadata specific to ServiceNow. </p>"""
    singular: NotRequired["aws_sdk_appflow.types.singular_metadata.SingularMetadata"]
    """<p> The connector metadata specific to Singular. </p>"""
    slack: NotRequired["aws_sdk_appflow.types.slack_metadata.SlackMetadata"]
    """<p> The connector metadata specific to Slack. </p>"""
    snowflake: NotRequired["aws_sdk_appflow.types.snowflake_metadata.SnowflakeMetadata"]
    """<p> The connector metadata specific to Snowflake. </p>"""
    trendmicro: NotRequired[
        "aws_sdk_appflow.types.trendmicro_metadata.TrendmicroMetadata"
    ]
    """<p> The connector metadata specific to Trend Micro. </p>"""
    veeva: NotRequired["aws_sdk_appflow.types.veeva_metadata.VeevaMetadata"]
    """<p> The connector metadata specific to Veeva. </p>"""
    zendesk: NotRequired["aws_sdk_appflow.types.zendesk_metadata.ZendeskMetadata"]
    """<p> The connector metadata specific to Zendesk. </p>"""
    event_bridge: NotRequired[
        "aws_sdk_appflow.types.event_bridge_metadata.EventBridgeMetadata"
    ]
    """<p> The connector metadata specific to Amazon EventBridge. </p>"""
    upsolver: NotRequired["aws_sdk_appflow.types.upsolver_metadata.UpsolverMetadata"]
    """<p> The connector metadata specific to Upsolver. </p>"""
    customer_profiles: NotRequired[
        "aws_sdk_appflow.types.customer_profiles_metadata.CustomerProfilesMetadata"
    ]
    """<p> The connector metadata specific to Connect Customer Customer Profiles. </p>"""
    honeycode: NotRequired["aws_sdk_appflow.types.honeycode_metadata.HoneycodeMetadata"]
    """<p> The connector metadata specific to Amazon Honeycode. </p>"""
    sapo_data: NotRequired["aws_sdk_appflow.types.sapo_data_metadata.SAPODataMetadata"]
    pardot: NotRequired["aws_sdk_appflow.types.pardot_metadata.PardotMetadata"]
    """<p>The connector metadata specific to Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorMetadata) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import aws_sdk_appflow.types.amplitude_metadata

        out["Amplitude"] = aws_sdk_appflow.types.amplitude_metadata.serialize_json(
            value["amplitude"]
        )
    if "datadog" in value:
        import aws_sdk_appflow.types.datadog_metadata

        out["Datadog"] = aws_sdk_appflow.types.datadog_metadata.serialize_json(
            value["datadog"]
        )
    if "dynatrace" in value:
        import aws_sdk_appflow.types.dynatrace_metadata

        out["Dynatrace"] = aws_sdk_appflow.types.dynatrace_metadata.serialize_json(
            value["dynatrace"]
        )
    if "google_analytics" in value:
        import aws_sdk_appflow.types.google_analytics_metadata

        out["GoogleAnalytics"] = (
            aws_sdk_appflow.types.google_analytics_metadata.serialize_json(
                value["google_analytics"]
            )
        )
    if "infor_nexus" in value:
        import aws_sdk_appflow.types.infor_nexus_metadata

        out["InforNexus"] = aws_sdk_appflow.types.infor_nexus_metadata.serialize_json(
            value["infor_nexus"]
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_metadata

        out["Marketo"] = aws_sdk_appflow.types.marketo_metadata.serialize_json(
            value["marketo"]
        )
    if "redshift" in value:
        import aws_sdk_appflow.types.redshift_metadata

        out["Redshift"] = aws_sdk_appflow.types.redshift_metadata.serialize_json(
            value["redshift"]
        )
    if "s3" in value:
        import aws_sdk_appflow.types.s3_metadata

        out["S3"] = aws_sdk_appflow.types.s3_metadata.serialize_json(value["s3"])
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_metadata

        out["Salesforce"] = aws_sdk_appflow.types.salesforce_metadata.serialize_json(
            value["salesforce"]
        )
    if "service_now" in value:
        import aws_sdk_appflow.types.service_now_metadata

        out["ServiceNow"] = aws_sdk_appflow.types.service_now_metadata.serialize_json(
            value["service_now"]
        )
    if "singular" in value:
        import aws_sdk_appflow.types.singular_metadata

        out["Singular"] = aws_sdk_appflow.types.singular_metadata.serialize_json(
            value["singular"]
        )
    if "slack" in value:
        import aws_sdk_appflow.types.slack_metadata

        out["Slack"] = aws_sdk_appflow.types.slack_metadata.serialize_json(
            value["slack"]
        )
    if "snowflake" in value:
        import aws_sdk_appflow.types.snowflake_metadata

        out["Snowflake"] = aws_sdk_appflow.types.snowflake_metadata.serialize_json(
            value["snowflake"]
        )
    if "trendmicro" in value:
        import aws_sdk_appflow.types.trendmicro_metadata

        out["Trendmicro"] = aws_sdk_appflow.types.trendmicro_metadata.serialize_json(
            value["trendmicro"]
        )
    if "veeva" in value:
        import aws_sdk_appflow.types.veeva_metadata

        out["Veeva"] = aws_sdk_appflow.types.veeva_metadata.serialize_json(
            value["veeva"]
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_metadata

        out["Zendesk"] = aws_sdk_appflow.types.zendesk_metadata.serialize_json(
            value["zendesk"]
        )
    if "event_bridge" in value:
        import aws_sdk_appflow.types.event_bridge_metadata

        out["EventBridge"] = aws_sdk_appflow.types.event_bridge_metadata.serialize_json(
            value["event_bridge"]
        )
    if "upsolver" in value:
        import aws_sdk_appflow.types.upsolver_metadata

        out["Upsolver"] = aws_sdk_appflow.types.upsolver_metadata.serialize_json(
            value["upsolver"]
        )
    if "customer_profiles" in value:
        import aws_sdk_appflow.types.customer_profiles_metadata

        out["CustomerProfiles"] = (
            aws_sdk_appflow.types.customer_profiles_metadata.serialize_json(
                value["customer_profiles"]
            )
        )
    if "honeycode" in value:
        import aws_sdk_appflow.types.honeycode_metadata

        out["Honeycode"] = aws_sdk_appflow.types.honeycode_metadata.serialize_json(
            value["honeycode"]
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_metadata

        out["SAPOData"] = aws_sdk_appflow.types.sapo_data_metadata.serialize_json(
            value["sapo_data"]
        )
    if "pardot" in value:
        import aws_sdk_appflow.types.pardot_metadata

        out["Pardot"] = aws_sdk_appflow.types.pardot_metadata.serialize_json(
            value["pardot"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorMetadata:
    out: ConnectorMetadata = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import aws_sdk_appflow.types.amplitude_metadata

        out["amplitude"] = aws_sdk_appflow.types.amplitude_metadata.deserialize_json(
            data["Amplitude"]
        )
    if "Datadog" in data:
        import aws_sdk_appflow.types.datadog_metadata

        out["datadog"] = aws_sdk_appflow.types.datadog_metadata.deserialize_json(
            data["Datadog"]
        )
    if "Dynatrace" in data:
        import aws_sdk_appflow.types.dynatrace_metadata

        out["dynatrace"] = aws_sdk_appflow.types.dynatrace_metadata.deserialize_json(
            data["Dynatrace"]
        )
    if "GoogleAnalytics" in data:
        import aws_sdk_appflow.types.google_analytics_metadata

        out["google_analytics"] = (
            aws_sdk_appflow.types.google_analytics_metadata.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "InforNexus" in data:
        import aws_sdk_appflow.types.infor_nexus_metadata

        out["infor_nexus"] = (
            aws_sdk_appflow.types.infor_nexus_metadata.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_metadata

        out["marketo"] = aws_sdk_appflow.types.marketo_metadata.deserialize_json(
            data["Marketo"]
        )
    if "Redshift" in data:
        import aws_sdk_appflow.types.redshift_metadata

        out["redshift"] = aws_sdk_appflow.types.redshift_metadata.deserialize_json(
            data["Redshift"]
        )
    if "S3" in data:
        import aws_sdk_appflow.types.s3_metadata

        out["s3"] = aws_sdk_appflow.types.s3_metadata.deserialize_json(data["S3"])
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_metadata

        out["salesforce"] = aws_sdk_appflow.types.salesforce_metadata.deserialize_json(
            data["Salesforce"]
        )
    if "ServiceNow" in data:
        import aws_sdk_appflow.types.service_now_metadata

        out["service_now"] = (
            aws_sdk_appflow.types.service_now_metadata.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import aws_sdk_appflow.types.singular_metadata

        out["singular"] = aws_sdk_appflow.types.singular_metadata.deserialize_json(
            data["Singular"]
        )
    if "Slack" in data:
        import aws_sdk_appflow.types.slack_metadata

        out["slack"] = aws_sdk_appflow.types.slack_metadata.deserialize_json(
            data["Slack"]
        )
    if "Snowflake" in data:
        import aws_sdk_appflow.types.snowflake_metadata

        out["snowflake"] = aws_sdk_appflow.types.snowflake_metadata.deserialize_json(
            data["Snowflake"]
        )
    if "Trendmicro" in data:
        import aws_sdk_appflow.types.trendmicro_metadata

        out["trendmicro"] = aws_sdk_appflow.types.trendmicro_metadata.deserialize_json(
            data["Trendmicro"]
        )
    if "Veeva" in data:
        import aws_sdk_appflow.types.veeva_metadata

        out["veeva"] = aws_sdk_appflow.types.veeva_metadata.deserialize_json(
            data["Veeva"]
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_metadata

        out["zendesk"] = aws_sdk_appflow.types.zendesk_metadata.deserialize_json(
            data["Zendesk"]
        )
    if "EventBridge" in data:
        import aws_sdk_appflow.types.event_bridge_metadata

        out["event_bridge"] = (
            aws_sdk_appflow.types.event_bridge_metadata.deserialize_json(
                data["EventBridge"]
            )
        )
    if "Upsolver" in data:
        import aws_sdk_appflow.types.upsolver_metadata

        out["upsolver"] = aws_sdk_appflow.types.upsolver_metadata.deserialize_json(
            data["Upsolver"]
        )
    if "CustomerProfiles" in data:
        import aws_sdk_appflow.types.customer_profiles_metadata

        out["customer_profiles"] = (
            aws_sdk_appflow.types.customer_profiles_metadata.deserialize_json(
                data["CustomerProfiles"]
            )
        )
    if "Honeycode" in data:
        import aws_sdk_appflow.types.honeycode_metadata

        out["honeycode"] = aws_sdk_appflow.types.honeycode_metadata.deserialize_json(
            data["Honeycode"]
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_metadata

        out["sapo_data"] = aws_sdk_appflow.types.sapo_data_metadata.deserialize_json(
            data["SAPOData"]
        )
    if "Pardot" in data:
        import aws_sdk_appflow.types.pardot_metadata

        out["pardot"] = aws_sdk_appflow.types.pardot_metadata.deserialize_json(
            data["Pardot"]
        )
    return out
