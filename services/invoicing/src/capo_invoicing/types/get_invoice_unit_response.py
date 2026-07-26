"""Generated from Smithy shape ``com.amazonaws.invoicing#GetInvoiceUnitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_string
    import capo_invoicing.types.description_string
    import capo_invoicing.types.invoice_unit_arn_string
    import capo_invoicing.types.invoice_unit_name
    import capo_invoicing.types.invoice_unit_rule
    import capo_invoicing.types.last_modified_timestamp
    import capo_invoicing.types.tax_inheritance_disabled_flag


class GetInvoiceUnitResponse(TypedDict, closed=True):
    invoice_unit_arn: NotRequired[
        "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    ]
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    invoice_receiver: NotRequired[
        "capo_invoicing.types.account_id_string.AccountIdString"
    ]
    """<p> The Amazon Web Services account ID chosen to be the receiver of an invoice unit. All invoices generated for that invoice unit will be sent to this account ID. </p>"""
    name: NotRequired["capo_invoicing.types.invoice_unit_name.InvoiceUnitName"]
    """<p> The unique name of the invoice unit that is shown on the generated invoice. </p>"""
    description: NotRequired[
        "capo_invoicing.types.description_string.DescriptionString"
    ]
    """<p> The assigned description for an invoice unit. </p>"""
    tax_inheritance_disabled: NotRequired[
        "capo_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
    ]
    """<p> Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>"""
    rule: NotRequired["capo_invoicing.types.invoice_unit_rule.InvoiceUnitRule"]
    last_modified: NotRequired[
        "capo_invoicing.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p> The most recent date the invoice unit response was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInvoiceUnitResponse) -> dict:
    out: dict = {}
    if "invoice_unit_arn" in value:
        out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    if "invoice_receiver" in value:
        out["InvoiceReceiver"] = value["invoice_receiver"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tax_inheritance_disabled" in value:
        out["TaxInheritanceDisabled"] = value["tax_inheritance_disabled"]
    if "rule" in value:
        import capo_invoicing.types.invoice_unit_rule

        out["Rule"] = capo_invoicing.types.invoice_unit_rule.serialize_aws_json_1_0(
            value["rule"]
        )
    if "last_modified" in value:
        import capo_invoicing.types.last_modified_timestamp

        out["LastModified"] = (
            capo_invoicing.types.last_modified_timestamp.serialize_aws_json_1_0(
                value["last_modified"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInvoiceUnitResponse:
    out: GetInvoiceUnitResponse = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArn" in data:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    if "InvoiceReceiver" in data:
        out["invoice_receiver"] = data["InvoiceReceiver"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "TaxInheritanceDisabled" in data:
        out["tax_inheritance_disabled"] = data["TaxInheritanceDisabled"]
    if "Rule" in data:
        import capo_invoicing.types.invoice_unit_rule

        out["rule"] = capo_invoicing.types.invoice_unit_rule.deserialize_aws_json_1_0(
            data["Rule"]
        )
    if "LastModified" in data:
        import capo_invoicing.types.last_modified_timestamp

        out["last_modified"] = (
            capo_invoicing.types.last_modified_timestamp.deserialize_aws_json_1_0(
                data["LastModified"]
            )
        )
    return out
