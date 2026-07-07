"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceConnectorProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.marketo_source_properties
    import aws_sdk_customer_profiles.types.s3_source_properties
    import aws_sdk_customer_profiles.types.salesforce_source_properties
    import aws_sdk_customer_profiles.types.service_now_source_properties
    import aws_sdk_customer_profiles.types.zendesk_source_properties


class SourceConnectorProperties(TypedDict, closed=True):
    marketo: NotRequired[
        "aws_sdk_customer_profiles.types.marketo_source_properties.MarketoSourceProperties"
    ]
    """<p>The properties that are applied when Marketo is being used as a source.</p>"""
    s3: NotRequired[
        "aws_sdk_customer_profiles.types.s3_source_properties.S3SourceProperties"
    ]
    """<p>The properties that are applied when Amazon S3 is being used as the flow source.</p>"""
    salesforce: NotRequired[
        "aws_sdk_customer_profiles.types.salesforce_source_properties.SalesforceSourceProperties"
    ]
    """<p>The properties that are applied when Salesforce is being used as a source.</p>"""
    service_now: NotRequired[
        "aws_sdk_customer_profiles.types.service_now_source_properties.ServiceNowSourceProperties"
    ]
    """<p>The properties that are applied when ServiceNow is being used as a source.</p>"""
    zendesk: NotRequired[
        "aws_sdk_customer_profiles.types.zendesk_source_properties.ZendeskSourceProperties"
    ]
    """<p>The properties that are applied when using Zendesk as a flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConnectorProperties) -> dict:
    out: dict = {}
    if "marketo" in value:
        import aws_sdk_customer_profiles.types.marketo_source_properties

        out["Marketo"] = (
            aws_sdk_customer_profiles.types.marketo_source_properties.serialize_json(
                value["marketo"]
            )
        )
    if "s3" in value:
        import aws_sdk_customer_profiles.types.s3_source_properties

        out["S3"] = aws_sdk_customer_profiles.types.s3_source_properties.serialize_json(
            value["s3"]
        )
    if "salesforce" in value:
        import aws_sdk_customer_profiles.types.salesforce_source_properties

        out["Salesforce"] = (
            aws_sdk_customer_profiles.types.salesforce_source_properties.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import aws_sdk_customer_profiles.types.service_now_source_properties

        out["ServiceNow"] = (
            aws_sdk_customer_profiles.types.service_now_source_properties.serialize_json(
                value["service_now"]
            )
        )
    if "zendesk" in value:
        import aws_sdk_customer_profiles.types.zendesk_source_properties

        out["Zendesk"] = (
            aws_sdk_customer_profiles.types.zendesk_source_properties.serialize_json(
                value["zendesk"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceConnectorProperties:
    out: SourceConnectorProperties = {}  # type: ignore[typeddict-item]
    if "Marketo" in data:
        import aws_sdk_customer_profiles.types.marketo_source_properties

        out["marketo"] = (
            aws_sdk_customer_profiles.types.marketo_source_properties.deserialize_json(
                data["Marketo"]
            )
        )
    if "S3" in data:
        import aws_sdk_customer_profiles.types.s3_source_properties

        out["s3"] = (
            aws_sdk_customer_profiles.types.s3_source_properties.deserialize_json(
                data["S3"]
            )
        )
    if "Salesforce" in data:
        import aws_sdk_customer_profiles.types.salesforce_source_properties

        out["salesforce"] = (
            aws_sdk_customer_profiles.types.salesforce_source_properties.deserialize_json(
                data["Salesforce"]
            )
        )
    if "ServiceNow" in data:
        import aws_sdk_customer_profiles.types.service_now_source_properties

        out["service_now"] = (
            aws_sdk_customer_profiles.types.service_now_source_properties.deserialize_json(
                data["ServiceNow"]
            )
        )
    if "Zendesk" in data:
        import aws_sdk_customer_profiles.types.zendesk_source_properties

        out["zendesk"] = (
            aws_sdk_customer_profiles.types.zendesk_source_properties.deserialize_json(
                data["Zendesk"]
            )
        )
    return out
