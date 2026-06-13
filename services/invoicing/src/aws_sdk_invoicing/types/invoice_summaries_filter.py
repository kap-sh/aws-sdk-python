"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceSummariesFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.billing_period
    import aws_sdk_invoicing.types.date_interval
    import aws_sdk_invoicing.types.receiver_role


class InvoiceSummariesFilter(TypedDict):
    time_interval: NotRequired["aws_sdk_invoicing.types.date_interval.DateInterval"]
    """<p>The date range for invoice summary retrieval. </p>"""
    billing_period: NotRequired["aws_sdk_invoicing.types.billing_period.BillingPeriod"]
    """<p>The billing period associated with the invoice documents. </p>"""
    invoicing_entity: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The name of the entity that issues the Amazon Web Services invoice.</p>"""
    receiver_role: NotRequired["aws_sdk_invoicing.types.receiver_role.ReceiverRole"]
    """<p>The role of the invoice receiver to filter by.</p> <note> <p>When <code>ReceiverRole</code> is specified:</p> <ul> <li> <p>Data is available starting <code>2025-06-01</code>. Queries for periods before <code>2025-06-01</code> return a validation error.</p> </li> <li> <p> <code>TimeInterval</code> supports a time interval of up to 5 years. Without <code>ReceiverRole</code>, <code>TimeInterval</code> is limited to one month.</p> </li> </ul> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceSummariesFilter) -> dict:
    out: dict = {}
    if "time_interval" in value:
        import aws_sdk_invoicing.types.date_interval

        out["TimeInterval"] = (
            aws_sdk_invoicing.types.date_interval.serialize_aws_json_1_0(
                value["time_interval"]
            )
        )
    if "billing_period" in value:
        import aws_sdk_invoicing.types.billing_period

        out["BillingPeriod"] = (
            aws_sdk_invoicing.types.billing_period.serialize_aws_json_1_0(
                value["billing_period"]
            )
        )
    if "invoicing_entity" in value:
        out["InvoicingEntity"] = value["invoicing_entity"]
    if "receiver_role" in value:
        import aws_sdk_invoicing.types.receiver_role

        out["ReceiverRole"] = (
            aws_sdk_invoicing.types.receiver_role.serialize_aws_json_1_0(
                value["receiver_role"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceSummariesFilter:
    out: InvoiceSummariesFilter = {}  # type: ignore[typeddict-item]
    if "TimeInterval" in data:
        import aws_sdk_invoicing.types.date_interval

        out["time_interval"] = (
            aws_sdk_invoicing.types.date_interval.deserialize_aws_json_1_0(
                data["TimeInterval"]
            )
        )
    if "BillingPeriod" in data:
        import aws_sdk_invoicing.types.billing_period

        out["billing_period"] = (
            aws_sdk_invoicing.types.billing_period.deserialize_aws_json_1_0(
                data["BillingPeriod"]
            )
        )
    if "InvoicingEntity" in data:
        out["invoicing_entity"] = data["InvoicingEntity"]
    if "ReceiverRole" in data:
        import aws_sdk_invoicing.types.receiver_role

        out["receiver_role"] = (
            aws_sdk_invoicing.types.receiver_role.deserialize_aws_json_1_0(
                data["ReceiverRole"]
            )
        )
    return out
