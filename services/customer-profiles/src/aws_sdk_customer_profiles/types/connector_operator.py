"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConnectorOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.marketo_connector_operator
    import aws_sdk_customer_profiles.types.s3_connector_operator
    import aws_sdk_customer_profiles.types.salesforce_connector_operator
    import aws_sdk_customer_profiles.types.service_now_connector_operator
    import aws_sdk_customer_profiles.types.zendesk_connector_operator


class ConnectorOperator(TypedDict, closed=True):
    marketo: NotRequired[
        "aws_sdk_customer_profiles.types.marketo_connector_operator.MarketoConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Marketo source fields.</p>"""
    s3: NotRequired[
        "aws_sdk_customer_profiles.types.s3_connector_operator.S3ConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Amazon S3 source fields.</p>"""
    salesforce: NotRequired[
        "aws_sdk_customer_profiles.types.salesforce_connector_operator.SalesforceConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Salesforce source fields.</p>"""
    service_now: NotRequired[
        "aws_sdk_customer_profiles.types.service_now_connector_operator.ServiceNowConnectorOperator"
    ]
    """<p>The operation to be performed on the provided ServiceNow source fields.</p>"""
    zendesk: NotRequired[
        "aws_sdk_customer_profiles.types.zendesk_connector_operator.ZendeskConnectorOperator"
    ]
    """<p>The operation to be performed on the provided Zendesk source fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOperator) -> dict:
    out: dict = {}
    if "marketo" in value:
        import aws_sdk_customer_profiles.types.marketo_connector_operator

        out["Marketo"] = (
            aws_sdk_customer_profiles.types.marketo_connector_operator.serialize_json(
                value["marketo"]
            )
        )
    if "s3" in value:
        import aws_sdk_customer_profiles.types.s3_connector_operator

        out["S3"] = (
            aws_sdk_customer_profiles.types.s3_connector_operator.serialize_json(
                value["s3"]
            )
        )
    if "salesforce" in value:
        import aws_sdk_customer_profiles.types.salesforce_connector_operator

        out["Salesforce"] = (
            aws_sdk_customer_profiles.types.salesforce_connector_operator.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_customer_profiles.types.service_now_connector_operator

        out["ServiceNow"] = (
            aws_sdk_customer_profiles.types.service_now_connector_operator.serialize_json(
                value["service_now"]
            )
        )
    if "zendesk" in value:
        import aws_sdk_customer_profiles.types.zendesk_connector_operator

        out["Zendesk"] = (
            aws_sdk_customer_profiles.types.zendesk_connector_operator.serialize_json(
                value["zendesk"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorOperator:
    out: ConnectorOperator = {}  # type: ignore[typeddict-item]
    if "Marketo" in data:
        import aws_sdk_customer_profiles.types.marketo_connector_operator

        out["marketo"] = (
            aws_sdk_customer_profiles.types.marketo_connector_operator.deserialize_json(
                data["Marketo"]
            )
        )
    if "S3" in data:
        import aws_sdk_customer_profiles.types.s3_connector_operator

        out["s3"] = (
            aws_sdk_customer_profiles.types.s3_connector_operator.deserialize_json(
                data["S3"]
            )
        )
    if "Salesforce" in data:
        import aws_sdk_customer_profiles.types.salesforce_connector_operator

        out["salesforce"] = (
            aws_sdk_customer_profiles.types.salesforce_connector_operator.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_customer_profiles.types.service_now_connector_operator

        out["service_now"] = (
            aws_sdk_customer_profiles.types.service_now_connector_operator.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Zendesk" in data:
        import aws_sdk_customer_profiles.types.zendesk_connector_operator

        out["zendesk"] = (
            aws_sdk_customer_profiles.types.zendesk_connector_operator.deserialize_json(
                data["Zendesk"]
            )
        )
    return out
