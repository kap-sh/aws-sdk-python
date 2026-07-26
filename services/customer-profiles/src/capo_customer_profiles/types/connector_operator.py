"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConnectorOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.marketo_connector_operator
    import capo_customer_profiles.types.s3_connector_operator
    import capo_customer_profiles.types.salesforce_connector_operator
    import capo_customer_profiles.types.service_now_connector_operator
    import capo_customer_profiles.types.zendesk_connector_operator


class ConnectorOperator(TypedDict, closed=True):
    marketo: NotRequired[
        "capo_customer_profiles.types.marketo_connector_operator.MarketoConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Marketo source fields.</p>"""
    s3: NotRequired[
        "capo_customer_profiles.types.s3_connector_operator.S3ConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Amazon S3 source fields.</p>"""
    salesforce: NotRequired[
        "capo_customer_profiles.types.salesforce_connector_operator.SalesforceConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Salesforce source fields.</p>"""
    service_now: NotRequired[
        "capo_customer_profiles.types.service_now_connector_operator.ServiceNowConnectorOperator"
    ]
    """<p>The operation to be performed on the provided ServiceNow source fields.</p>"""
    zendesk: NotRequired[
        "capo_customer_profiles.types.zendesk_connector_operator.ZendeskConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Zendesk source fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOperator) -> dict:
    out: dict = {}
    if "marketo" in value:
        import capo_customer_profiles.types.marketo_connector_operator

        out["Marketo"] = (
            capo_customer_profiles.types.marketo_connector_operator.serialize_json(
                value["marketo"]
            )
        )
    if "s3" in value:
        import capo_customer_profiles.types.s3_connector_operator

        out["S3"] = capo_customer_profiles.types.s3_connector_operator.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import capo_customer_profiles.types.salesforce_connector_operator

        out["Salesforce"] = (
            capo_customer_profiles.types.salesforce_connector_operator.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import capo_customer_profiles.types.service_now_connector_operator

        out["ServiceNow"] = (
            capo_customer_profiles.types.service_now_connector_operator.serialize_json(
                value["service_now"]
            )
        )
    if "zendesk" in value:
        import capo_customer_profiles.types.zendesk_connector_operator

        out["Zendesk"] = (
            capo_customer_profiles.types.zendesk_connector_operator.serialize_json(
                value["zendesk"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorOperator:
    out: ConnectorOperator = {}  # type: ignore[typeddict-item]
    if "Marketo" in data:
        import capo_customer_profiles.types.marketo_connector_operator

        out["marketo"] = (
            capo_customer_profiles.types.marketo_connector_operator.deserialize_json(
                data["Marketo"]
            )
        )
    if "S3" in data:
        import capo_customer_profiles.types.s3_connector_operator

        out["s3"] = capo_customer_profiles.types.s3_connector_operator.deserialize_json(
            data["S3"]
        )
    if "Salesforce" in data:
        import capo_customer_profiles.types.salesforce_connector_operator

        out["salesforce"] = (
            capo_customer_profiles.types.salesforce_connector_operator.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import capo_customer_profiles.types.service_now_connector_operator

        out["service_now"] = (
            capo_customer_profiles.types.service_now_connector_operator.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Zendesk" in data:
        import capo_customer_profiles.types.zendesk_connector_operator

        out["zendesk"] = (
            capo_customer_profiles.types.zendesk_connector_operator.deserialize_json(
                data["Zendesk"]
            )
        )
    return out
