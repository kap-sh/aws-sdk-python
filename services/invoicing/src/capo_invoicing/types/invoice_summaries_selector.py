"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceSummariesSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.list_invoice_summaries_resource_type
    import capo_invoicing.types.string_without_new_line


class InvoiceSummariesSelector(TypedDict, closed=True):
    resource_type: "capo_invoicing.types.list_invoice_summaries_resource_type.ListInvoiceSummariesResourceType"
    """<p>The query identifier type (<code>INVOICE_ID</code> or <code>ACCOUNT_ID</code>).</p>"""
    value: "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    """<p>The value of the query identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceSummariesSelector) -> dict:
    out: dict = {}
    import capo_invoicing.types.list_invoice_summaries_resource_type

    out["ResourceType"] = (
        capo_invoicing.types.list_invoice_summaries_resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceSummariesSelector:
    out: InvoiceSummariesSelector = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_invoicing.types.list_invoice_summaries_resource_type

        out["resource_type"] = (
            capo_invoicing.types.list_invoice_summaries_resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("InvoiceSummariesSelector.resource_type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("InvoiceSummariesSelector.value required")
    return out
