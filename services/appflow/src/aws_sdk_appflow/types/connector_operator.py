"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.amplitude_connector_operator
    import aws_sdk_appflow.types.datadog_connector_operator
    import aws_sdk_appflow.types.dynatrace_connector_operator
    import aws_sdk_appflow.types.google_analytics_connector_operator
    import aws_sdk_appflow.types.infor_nexus_connector_operator
    import aws_sdk_appflow.types.marketo_connector_operator
    import aws_sdk_appflow.types.operator
    import aws_sdk_appflow.types.pardot_connector_operator
    import aws_sdk_appflow.types.s3_connector_operator
    import aws_sdk_appflow.types.salesforce_connector_operator
    import aws_sdk_appflow.types.sapo_data_connector_operator
    import aws_sdk_appflow.types.service_now_connector_operator
    import aws_sdk_appflow.types.singular_connector_operator
    import aws_sdk_appflow.types.slack_connector_operator
    import aws_sdk_appflow.types.trendmicro_connector_operator
    import aws_sdk_appflow.types.veeva_connector_operator
    import aws_sdk_appflow.types.zendesk_connector_operator


class ConnectorOperator(TypedDict, closed=True):
    amplitude: NotRequired[
        "aws_sdk_appflow.types.amplitude_connector_operator.AmplitudeConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Amplitude source fields. </p>"""
    datadog: NotRequired[
        "aws_sdk_appflow.types.datadog_connector_operator.DatadogConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Datadog source fields. </p>"""
    dynatrace: NotRequired[
        "aws_sdk_appflow.types.dynatrace_connector_operator.DynatraceConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Dynatrace source fields. </p>"""
    google_analytics: NotRequired[
        "aws_sdk_appflow.types.google_analytics_connector_operator.GoogleAnalyticsConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Google Analytics source fields. </p>"""
    infor_nexus: NotRequired[
        "aws_sdk_appflow.types.infor_nexus_connector_operator.InforNexusConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Infor Nexus source fields. </p>"""
    marketo: NotRequired[
        "aws_sdk_appflow.types.marketo_connector_operator.MarketoConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Marketo source fields. </p>"""
    s3: NotRequired["aws_sdk_appflow.types.s3_connector_operator.S3ConnectorOperator"]
    """<p> The operation to be performed on the provided Amazon S3 source fields. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_connector_operator.SalesforceConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Salesforce source fields. </p>"""
    service_now: NotRequired[
        "aws_sdk_appflow.types.service_now_connector_operator.ServiceNowConnectorOperator"
    ]
    """<p> The operation to be performed on the provided ServiceNow source fields. </p>"""
    singular: NotRequired[
        "aws_sdk_appflow.types.singular_connector_operator.SingularConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Singular source fields. </p>"""
    slack: NotRequired[
        "aws_sdk_appflow.types.slack_connector_operator.SlackConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Slack source fields. </p>"""
    trendmicro: NotRequired[
        "aws_sdk_appflow.types.trendmicro_connector_operator.TrendmicroConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Trend Micro source fields. </p>"""
    veeva: NotRequired[
        "aws_sdk_appflow.types.veeva_connector_operator.VeevaConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Veeva source fields. </p>"""
    zendesk: NotRequired[
        "aws_sdk_appflow.types.zendesk_connector_operator.ZendeskConnectorOperator"
    ]
    """<p> The operation to be performed on the provided Zendesk source fields. </p>"""
    sapo_data: NotRequired[
        "aws_sdk_appflow.types.sapo_data_connector_operator.SAPODataConnectorOperator"
    ]
    """<p> The operation to be performed on the provided SAPOData source fields. </p>"""
    custom_connector: NotRequired["aws_sdk_appflow.types.operator.Operator"]
    """<p>Operators supported by the custom connector.</p>"""
    pardot: NotRequired[
        "aws_sdk_appflow.types.pardot_connector_operator.PardotConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Salesforce Pardot source fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOperator) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import aws_sdk_appflow.types.amplitude_connector_operator

        out["Amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_operator.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import aws_sdk_appflow.types.datadog_connector_operator

        out["Datadog"] = (
            aws_sdk_appflow.types.datadog_connector_operator.serialize_json(
                value["datadog"]
            )
        )
    if "dynatrace" in value:
        import aws_sdk_appflow.types.dynatrace_connector_operator

        out["Dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_operator.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import aws_sdk_appflow.types.google_analytics_connector_operator

        out["GoogleAnalytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_operator.serialize_json(
                value["google_analytics"]
            )
        )
    if "infor_nexus" in value:
        import aws_sdk_appflow.types.infor_nexus_connector_operator

        out["InforNexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_operator.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_connector_operator

        out["Marketo"] = (
            aws_sdk_appflow.types.marketo_connector_operator.serialize_json(
                value["marketo"]
            )
        )
    if "s3" in value:
        import aws_sdk_appflow.types.s3_connector_operator

        out["S3"] = aws_sdk_appflow.types.s3_connector_operator.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_connector_operator

        out["Salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_operator.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_appflow.types.service_now_connector_operator

        out["ServiceNow"] = (
            aws_sdk_appflow.types.service_now_connector_operator.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import aws_sdk_appflow.types.singular_connector_operator

        out["Singular"] = (
            aws_sdk_appflow.types.singular_connector_operator.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import aws_sdk_appflow.types.slack_connector_operator

        out["Slack"] = aws_sdk_appflow.types.slack_connector_operator.serialize_json(
            value["slack"]
        )
    if "trendmicro" in value:
        import aws_sdk_appflow.types.trendmicro_connector_operator

        out["Trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_operator.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import aws_sdk_appflow.types.veeva_connector_operator

        out["Veeva"] = aws_sdk_appflow.types.veeva_connector_operator.serialize_json(
            value["veeva"]
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_connector_operator

        out["Zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_operator.serialize_json(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_connector_operator

        out["SAPOData"] = (
            aws_sdk_appflow.types.sapo_data_connector_operator.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import aws_sdk_appflow.types.operator

        out["CustomConnector"] = aws_sdk_appflow.types.operator.serialize_json(
            value["custom_connector"]
        )
    if "pardot" in value:
        import aws_sdk_appflow.types.pardot_connector_operator

        out["Pardot"] = aws_sdk_appflow.types.pardot_connector_operator.serialize_json(
            value["pardot"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorOperator:
    out: ConnectorOperator = {}  # type: ignore[typeddict-item]
    if "Amplitude" in data:
        import aws_sdk_appflow.types.amplitude_connector_operator

        out["amplitude"] = (
            aws_sdk_appflow.types.amplitude_connector_operator.deserialize_json(
                data["Amplitude"]
            )
        )
    if "Datadog" in data:
        import aws_sdk_appflow.types.datadog_connector_operator

        out["datadog"] = (
            aws_sdk_appflow.types.datadog_connector_operator.deserialize_json(
                data["Datadog"]
            )
        )
    if "Dynatrace" in data:
        import aws_sdk_appflow.types.dynatrace_connector_operator

        out["dynatrace"] = (
            aws_sdk_appflow.types.dynatrace_connector_operator.deserialize_json(
                data["Dynatrace"]
            )
        )
    if "GoogleAnalytics" in data:
        import aws_sdk_appflow.types.google_analytics_connector_operator

        out["google_analytics"] = (
            aws_sdk_appflow.types.google_analytics_connector_operator.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if "InforNexus" in data:
        import aws_sdk_appflow.types.infor_nexus_connector_operator

        out["infor_nexus"] = (
            aws_sdk_appflow.types.infor_nexus_connector_operator.deserialize_json(
                data["InforNexus"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_connector_operator

        out["marketo"] = (
            aws_sdk_appflow.types.marketo_connector_operator.deserialize_json(
                data["Marketo"]
            )
        )
    if "S3" in data:
        import aws_sdk_appflow.types.s3_connector_operator

        out["s3"] = aws_sdk_appflow.types.s3_connector_operator.deserialize_json(
            data["S3"]
        )
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_connector_operator

        out["salesforce"] = (
            aws_sdk_appflow.types.salesforce_connector_operator.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_appflow.types.service_now_connector_operator

        out["service_now"] = (
            aws_sdk_appflow.types.service_now_connector_operator.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Singular" in data:
        import aws_sdk_appflow.types.singular_connector_operator

        out["singular"] = (
            aws_sdk_appflow.types.singular_connector_operator.deserialize_json(
                data["Singular"]
            )
        )
    if "Slack" in data:
        import aws_sdk_appflow.types.slack_connector_operator

        out["slack"] = aws_sdk_appflow.types.slack_connector_operator.deserialize_json(
            data["Slack"]
        )
    if "Trendmicro" in data:
        import aws_sdk_appflow.types.trendmicro_connector_operator

        out["trendmicro"] = (
            aws_sdk_appflow.types.trendmicro_connector_operator.deserialize_json(
                data["Trendmicro"]
            )
        )
    if "Veeva" in data:
        import aws_sdk_appflow.types.veeva_connector_operator

        out["veeva"] = aws_sdk_appflow.types.veeva_connector_operator.deserialize_json(
            data["Veeva"]
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_connector_operator

        out["zendesk"] = (
            aws_sdk_appflow.types.zendesk_connector_operator.deserialize_json(
                data["Zendesk"]
            )
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_connector_operator

        out["sapo_data"] = (
            aws_sdk_appflow.types.sapo_data_connector_operator.deserialize_json(
                data["SAPOData"]
            )
        )
    if "CustomConnector" in data:
        import aws_sdk_appflow.types.operator

        out["custom_connector"] = aws_sdk_appflow.types.operator.deserialize_json(
            data["CustomConnector"]
        )
    if "Pardot" in data:
        import aws_sdk_appflow.types.pardot_connector_operator

        out["pardot"] = (
            aws_sdk_appflow.types.pardot_connector_operator.deserialize_json(
                data["Pardot"]
            )
        )
    return out
