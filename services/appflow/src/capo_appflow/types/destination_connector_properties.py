"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationConnectorProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.custom_connector_destination_properties
    import capo_appflow.types.customer_profiles_destination_properties
    import capo_appflow.types.event_bridge_destination_properties
    import capo_appflow.types.honeycode_destination_properties
    import capo_appflow.types.lookout_metrics_destination_properties
    import capo_appflow.types.marketo_destination_properties
    import capo_appflow.types.redshift_destination_properties
    import capo_appflow.types.s3_destination_properties
    import capo_appflow.types.salesforce_destination_properties
    import capo_appflow.types.sapo_data_destination_properties
    import capo_appflow.types.snowflake_destination_properties
    import capo_appflow.types.upsolver_destination_properties
    import capo_appflow.types.zendesk_destination_properties


class DestinationConnectorProperties(TypedDict, closed=True):
    redshift: NotRequired[
        "capo_appflow.types.redshift_destination_properties.RedshiftDestinationProperties"
    ]
    """<p> The properties required to query Amazon Redshift. </p>"""
    s3: NotRequired[
        "capo_appflow.types.s3_destination_properties.S3DestinationProperties"
    ]
    """<p> The properties required to query Amazon S3. </p>"""
    salesforce: NotRequired[
        "capo_appflow.types.salesforce_destination_properties.SalesforceDestinationProperties"
    ]
    """<p> The properties required to query Salesforce. </p>"""
    snowflake: NotRequired[
        "capo_appflow.types.snowflake_destination_properties.SnowflakeDestinationProperties"
    ]
    """<p> The properties required to query Snowflake. </p>"""
    event_bridge: NotRequired[
        "capo_appflow.types.event_bridge_destination_properties.EventBridgeDestinationProperties"
    ]
    """<p> The properties required to query Amazon EventBridge. </p>"""
    lookout_metrics: NotRequired[
        "capo_appflow.types.lookout_metrics_destination_properties.LookoutMetricsDestinationProperties"
    ]
    """<p> The properties required to query Amazon Lookout for Metrics. </p>"""
    upsolver: NotRequired[
        "capo_appflow.types.upsolver_destination_properties.UpsolverDestinationProperties"
    ]
    """<p> The properties required to query Upsolver. </p>"""
    honeycode: NotRequired[
        "capo_appflow.types.honeycode_destination_properties.HoneycodeDestinationProperties"
    ]
    """<p> The properties required to query Amazon Honeycode. </p>"""
    customer_profiles: NotRequired[
        "capo_appflow.types.customer_profiles_destination_properties.CustomerProfilesDestinationProperties"
    ]
    """<p> The properties required to query Connect Customer Customer Profiles. </p>"""
    zendesk: NotRequired[
        "capo_appflow.types.zendesk_destination_properties.ZendeskDestinationProperties"
    ]
    """<p>The properties required to query Zendesk.</p>"""
    marketo: NotRequired[
        "capo_appflow.types.marketo_destination_properties.MarketoDestinationProperties"
    ]
    """<p>The properties required to query Marketo.</p>"""
    custom_connector: NotRequired[
        "capo_appflow.types.custom_connector_destination_properties.CustomConnectorDestinationProperties"
    ]
    """<p>The properties that are required to query the custom Connector.</p>"""
    sapo_data: NotRequired[
        "capo_appflow.types.sapo_data_destination_properties.SAPODataDestinationProperties"
    ]
    """<p>The properties required to query SAPOData.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConnectorProperties) -> dict:
    out: dict = {}
    if "redshift" in value:
        import capo_appflow.types.redshift_destination_properties

        out["Redshift"] = (
            capo_appflow.types.redshift_destination_properties.serialize_json(
                value["redshift"]
            )
        )
    if "s3" in value:
        import capo_appflow.types.s3_destination_properties

        out["S3"] = capo_appflow.types.s3_destination_properties.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import capo_appflow.types.salesforce_destination_properties

        out["Salesforce"] = (
            capo_appflow.types.salesforce_destination_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "snowflake" in value:
        import capo_appflow.types.snowflake_destination_properties

        out["Snowflake"] = (
            capo_appflow.types.snowflake_destination_properties.serialize_json(
                value["snowflake"]
            )
        )
    if "event_bridge" in value:
        import capo_appflow.types.event_bridge_destination_properties

        out["EventBridge"] = (
            capo_appflow.types.event_bridge_destination_properties.serialize_json(
                value["event_bridge"]
            )
        )
    if "lookout_metrics" in value:
        import capo_appflow.types.lookout_metrics_destination_properties

        out["LookoutMetrics"] = (
            capo_appflow.types.lookout_metrics_destination_properties.serialize_json(
                value["lookout_metrics"]
            )
        )
    if "upsolver" in value:
        import capo_appflow.types.upsolver_destination_properties

        out["Upsolver"] = (
            capo_appflow.types.upsolver_destination_properties.serialize_json(
                value["upsolver"]
            )
        )
    if "honeycode" in value:
        import capo_appflow.types.honeycode_destination_properties

        out["Honeycode"] = (
            capo_appflow.types.honeycode_destination_properties.serialize_json(
                value["honeycode"]
            )
        )
    if "customer_profiles" in value:
        import capo_appflow.types.customer_profiles_destination_properties

        out["CustomerProfiles"] = (
            capo_appflow.types.customer_profiles_destination_properties.serialize_json(
                value["customer_profiles"]
            )
        )
    if "zendesk" in value:
        import capo_appflow.types.zendesk_destination_properties

        out["Zendesk"] = (
            capo_appflow.types.zendesk_destination_properties.serialize_json(
                value["zendesk"]
            )
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_destination_properties

        out["Marketo"] = (
            capo_appflow.types.marketo_destination_properties.serialize_json(
                value["marketo"]
            )
        )
    if "custom_connector" in value:
        import capo_appflow.types.custom_connector_destination_properties

        out["CustomConnector"] = (
            capo_appflow.types.custom_connector_destination_properties.serialize_json(
                value["custom_connector"]
            )
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_destination_properties

        out["SAPOData"] = (
            capo_appflow.types.sapo_data_destination_properties.serialize_json(
                value["sapo_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationConnectorProperties:
    out: DestinationConnectorProperties = {}  # type: ignore[typeddict-item]
    if "Redshift" in data:
        import capo_appflow.types.redshift_destination_properties

        out["redshift"] = (
            capo_appflow.types.redshift_destination_properties.deserialize_json(
                data["Redshift"]
            )
        )
    if "S3" in data:
        import capo_appflow.types.s3_destination_properties

        out["s3"] = capo_appflow.types.s3_destination_properties.deserialize_json(
            data["S3"]
        )
    if "Salesforce" in data:
        import capo_appflow.types.salesforce_destination_properties

        out["salesforce"] = (
            capo_appflow.types.salesforce_destination_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "Snowflake" in data:
        import capo_appflow.types.snowflake_destination_properties

        out["snowflake"] = (
            capo_appflow.types.snowflake_destination_properties.deserialize_json(
                data["Snowflake"]
            )
        )
    if "EventBridge" in data:
        import capo_appflow.types.event_bridge_destination_properties

        out["event_bridge"] = (
            capo_appflow.types.event_bridge_destination_properties.deserialize_json(
                data["EventBridge"]
            )
        )
    if "LookoutMetrics" in data:
        import capo_appflow.types.lookout_metrics_destination_properties

        out["lookout_metrics"] = (
            capo_appflow.types.lookout_metrics_destination_properties.deserialize_json(
                data["LookoutMetrics"]
            )
        )
    if "Upsolver" in data:
        import capo_appflow.types.upsolver_destination_properties

        out["upsolver"] = (
            capo_appflow.types.upsolver_destination_properties.deserialize_json(
                data["Upsolver"]
            )
        )
    if "Honeycode" in data:
        import capo_appflow.types.honeycode_destination_properties

        out["honeycode"] = (
            capo_appflow.types.honeycode_destination_properties.deserialize_json(
                data["Honeycode"]
            )
        )
    if "CustomerProfiles" in data:
        import capo_appflow.types.customer_profiles_destination_properties

        out["customer_profiles"] = (
            capo_appflow.types.customer_profiles_destination_properties.deserialize_json(
                data["CustomerProfiles"]
            )
        )
    if "Zendesk" in data:
        import capo_appflow.types.zendesk_destination_properties

        out["zendesk"] = (
            capo_appflow.types.zendesk_destination_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    if "Marketo" in data:
        import capo_appflow.types.marketo_destination_properties

        out["marketo"] = (
            capo_appflow.types.marketo_destination_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "CustomConnector" in data:
        import capo_appflow.types.custom_connector_destination_properties

        out["custom_connector"] = (
            capo_appflow.types.custom_connector_destination_properties.deserialize_json(
                data["CustomConnector"]
            )
        )
    if "SAPOData" in data:
        import capo_appflow.types.sapo_data_destination_properties

        out["sapo_data"] = (
            capo_appflow.types.sapo_data_destination_properties.deserialize_json(
                data["SAPOData"]
            )
        )
    return out
