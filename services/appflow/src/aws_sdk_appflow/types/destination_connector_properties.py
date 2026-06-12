"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationConnectorProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.custom_connector_destination_properties
    import aws_sdk_appflow.types.customer_profiles_destination_properties
    import aws_sdk_appflow.types.event_bridge_destination_properties
    import aws_sdk_appflow.types.honeycode_destination_properties
    import aws_sdk_appflow.types.lookout_metrics_destination_properties
    import aws_sdk_appflow.types.marketo_destination_properties
    import aws_sdk_appflow.types.redshift_destination_properties
    import aws_sdk_appflow.types.s3_destination_properties
    import aws_sdk_appflow.types.salesforce_destination_properties
    import aws_sdk_appflow.types.sapo_data_destination_properties
    import aws_sdk_appflow.types.snowflake_destination_properties
    import aws_sdk_appflow.types.upsolver_destination_properties
    import aws_sdk_appflow.types.zendesk_destination_properties


class DestinationConnectorProperties(TypedDict):
    redshift: NotRequired[
        "aws_sdk_appflow.types.redshift_destination_properties.RedshiftDestinationProperties"
    ]
    """<p> The properties required to query Amazon Redshift. </p>"""
    s3: NotRequired[
        "aws_sdk_appflow.types.s3_destination_properties.S3DestinationProperties"
    ]
    """<p> The properties required to query Amazon S3. </p>"""
    salesforce: NotRequired[
        "aws_sdk_appflow.types.salesforce_destination_properties.SalesforceDestinationProperties"
    ]
    """<p> The properties required to query Salesforce. </p>"""
    snowflake: NotRequired[
        "aws_sdk_appflow.types.snowflake_destination_properties.SnowflakeDestinationProperties"
    ]
    """<p> The properties required to query Snowflake. </p>"""
    event_bridge: NotRequired[
        "aws_sdk_appflow.types.event_bridge_destination_properties.EventBridgeDestinationProperties"
    ]
    """<p> The properties required to query Amazon EventBridge. </p>"""
    lookout_metrics: NotRequired[
        "aws_sdk_appflow.types.lookout_metrics_destination_properties.LookoutMetricsDestinationProperties"
    ]
    """<p> The properties required to query Amazon Lookout for Metrics. </p>"""
    upsolver: NotRequired[
        "aws_sdk_appflow.types.upsolver_destination_properties.UpsolverDestinationProperties"
    ]
    """<p> The properties required to query Upsolver. </p>"""
    honeycode: NotRequired[
        "aws_sdk_appflow.types.honeycode_destination_properties.HoneycodeDestinationProperties"
    ]
    """<p> The properties required to query Amazon Honeycode. </p>"""
    customer_profiles: NotRequired[
        "aws_sdk_appflow.types.customer_profiles_destination_properties.CustomerProfilesDestinationProperties"
    ]
    """<p> The properties required to query Connect Customer Customer Profiles. </p>"""
    zendesk: NotRequired[
        "aws_sdk_appflow.types.zendesk_destination_properties.ZendeskDestinationProperties"
    ]
    """<p>The properties required to query Zendesk.</p>"""
    marketo: NotRequired[
        "aws_sdk_appflow.types.marketo_destination_properties.MarketoDestinationProperties"
    ]
    """<p>The properties required to query Marketo.</p>"""
    custom_connector: NotRequired[
        "aws_sdk_appflow.types.custom_connector_destination_properties.CustomConnectorDestinationProperties"
    ]
    """<p>The properties that are required to query the custom Connector.</p>"""
    sapo_data: NotRequired[
        "aws_sdk_appflow.types.sapo_data_destination_properties.SAPODataDestinationProperties"
    ]
    """<p>The properties required to query SAPOData.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConnectorProperties) -> dict:
    out: dict = {}
    if "redshift" in value:
        import aws_sdk_appflow.types.redshift_destination_properties

        out["Redshift"] = (
            aws_sdk_appflow.types.redshift_destination_properties.serialize_json(
                value["redshift"]
            )
        )
    if "s3" in value:
        import aws_sdk_appflow.types.s3_destination_properties

        out["S3"] = aws_sdk_appflow.types.s3_destination_properties.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import aws_sdk_appflow.types.salesforce_destination_properties

        out["Salesforce"] = (
            aws_sdk_appflow.types.salesforce_destination_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "snowflake" in value:
        import aws_sdk_appflow.types.snowflake_destination_properties

        out["Snowflake"] = (
            aws_sdk_appflow.types.snowflake_destination_properties.serialize_json(
                value["snowflake"]
            )
        )
    if "event_bridge" in value:
        import aws_sdk_appflow.types.event_bridge_destination_properties

        out["EventBridge"] = (
            aws_sdk_appflow.types.event_bridge_destination_properties.serialize_json(
                value["event_bridge"]
            )
        )
    if "lookout_metrics" in value:
        import aws_sdk_appflow.types.lookout_metrics_destination_properties

        out["LookoutMetrics"] = (
            aws_sdk_appflow.types.lookout_metrics_destination_properties.serialize_json(
                value["lookout_metrics"]
            )
        )
    if "upsolver" in value:
        import aws_sdk_appflow.types.upsolver_destination_properties

        out["Upsolver"] = (
            aws_sdk_appflow.types.upsolver_destination_properties.serialize_json(
                value["upsolver"]
            )
        )
    if "honeycode" in value:
        import aws_sdk_appflow.types.honeycode_destination_properties

        out["Honeycode"] = (
            aws_sdk_appflow.types.honeycode_destination_properties.serialize_json(
                value["honeycode"]
            )
        )
    if "customer_profiles" in value:
        import aws_sdk_appflow.types.customer_profiles_destination_properties

        out["CustomerProfiles"] = (
            aws_sdk_appflow.types.customer_profiles_destination_properties.serialize_json(
                value["customer_profiles"]
            )
        )
    if "zendesk" in value:
        import aws_sdk_appflow.types.zendesk_destination_properties

        out["Zendesk"] = (
            aws_sdk_appflow.types.zendesk_destination_properties.serialize_json(
                value["zendesk"]
            )
        )
    if "marketo" in value:
        import aws_sdk_appflow.types.marketo_destination_properties

        out["Marketo"] = (
            aws_sdk_appflow.types.marketo_destination_properties.serialize_json(
                value["marketo"]
            )
        )
    if "custom_connector" in value:
        import aws_sdk_appflow.types.custom_connector_destination_properties

        out["CustomConnector"] = (
            aws_sdk_appflow.types.custom_connector_destination_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "sapo_data" in value:
        import aws_sdk_appflow.types.sapo_data_destination_properties

        out["SAPOData"] = (
            aws_sdk_appflow.types.sapo_data_destination_properties.serialize_json(
                value["sapo_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationConnectorProperties:
    out: DestinationConnectorProperties = {}  # type: ignore[typeddict-item]
    if "Redshift" in data:
        import aws_sdk_appflow.types.redshift_destination_properties

        out["redshift"] = (
            aws_sdk_appflow.types.redshift_destination_properties.deserialize_json(
                data["Redshift"]
            )
        )
    if "S3" in data:
        import aws_sdk_appflow.types.s3_destination_properties

        out["s3"] = aws_sdk_appflow.types.s3_destination_properties.deserialize_json(
            data["S3"]
        )
    if "Salesforce" in data:
        import aws_sdk_appflow.types.salesforce_destination_properties

        out["salesforce"] = (
            aws_sdk_appflow.types.salesforce_destination_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "Snowflake" in data:
        import aws_sdk_appflow.types.snowflake_destination_properties

        out["snowflake"] = (
            aws_sdk_appflow.types.snowflake_destination_properties.deserialize_json(
                data["Snowflake"]
            )
        )
    if "EventBridge" in data:
        import aws_sdk_appflow.types.event_bridge_destination_properties

        out["event_bridge"] = (
            aws_sdk_appflow.types.event_bridge_destination_properties.deserialize_json(
                data["EventBridge"]
            )
        )
    if "LookoutMetrics" in data:
        import aws_sdk_appflow.types.lookout_metrics_destination_properties

        out["lookout_metrics"] = (
            aws_sdk_appflow.types.lookout_metrics_destination_properties.deserialize_json(
                data["LookoutMetrics"]
            )
        )
    if "Upsolver" in data:
        import aws_sdk_appflow.types.upsolver_destination_properties

        out["upsolver"] = (
            aws_sdk_appflow.types.upsolver_destination_properties.deserialize_json(
                data["Upsolver"]
            )
        )
    if "Honeycode" in data:
        import aws_sdk_appflow.types.honeycode_destination_properties

        out["honeycode"] = (
            aws_sdk_appflow.types.honeycode_destination_properties.deserialize_json(
                data["Honeycode"]
            )
        )
    if "CustomerProfiles" in data:
        import aws_sdk_appflow.types.customer_profiles_destination_properties

        out["customer_profiles"] = (
            aws_sdk_appflow.types.customer_profiles_destination_properties.deserialize_json(
                data["CustomerProfiles"]
            )
        )
    if "Zendesk" in data:
        import aws_sdk_appflow.types.zendesk_destination_properties

        out["zendesk"] = (
            aws_sdk_appflow.types.zendesk_destination_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    if "Marketo" in data:
        import aws_sdk_appflow.types.marketo_destination_properties

        out["marketo"] = (
            aws_sdk_appflow.types.marketo_destination_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "CustomConnector" in data:
        import aws_sdk_appflow.types.custom_connector_destination_properties

        out["custom_connector"] = (
            aws_sdk_appflow.types.custom_connector_destination_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "SAPOData" in data:
        import aws_sdk_appflow.types.sapo_data_destination_properties

        out["sapo_data"] = (
            aws_sdk_appflow.types.sapo_data_destination_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    return out
