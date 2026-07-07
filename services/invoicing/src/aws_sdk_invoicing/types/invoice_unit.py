"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_string
    import aws_sdk_invoicing.types.description_string
    import aws_sdk_invoicing.types.invoice_unit_arn_string
    import aws_sdk_invoicing.types.invoice_unit_name
    import aws_sdk_invoicing.types.invoice_unit_rule
    import aws_sdk_invoicing.types.last_modified_timestamp
    import aws_sdk_invoicing.types.tax_inheritance_disabled_flag


class InvoiceUnit(TypedDict, closed=True):
    invoice_unit_arn: NotRequired[
        "aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    ]
    """<p>ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    invoice_receiver: NotRequired[
        "aws_sdk_invoicing.types.account_id_string.AccountIdString"
    ]
    """<p>The account that receives invoices related to the invoice unit. </p>"""
    name: NotRequired["aws_sdk_invoicing.types.invoice_unit_name.InvoiceUnitName"]
    """<p> A unique name that is distinctive within your Amazon Web Services. </p>"""
    description: NotRequired[
        "aws_sdk_invoicing.types.description_string.DescriptionString"
    ]
    """<p>The assigned description for an invoice unit. This information can't be modified or deleted. </p>"""
    tax_inheritance_disabled: NotRequired[
        "aws_sdk_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
    ]
    """<p>Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>"""
    rule: NotRequired["aws_sdk_invoicing.types.invoice_unit_rule.InvoiceUnitRule"]
    """<p> An <code>InvoiceUnitRule</code> object used the categorize invoice units. </p>"""
    last_modified: NotRequired[
        "aws_sdk_invoicing.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p> The last time the invoice unit was updated. This is important to determine the version of invoice unit configuration used to create the invoices. Any invoice created after this modified time will use this invoice unit configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceUnit) -> dict:
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
        import aws_sdk_invoicing.types.invoice_unit_rule

        out["Rule"] = aws_sdk_invoicing.types.invoice_unit_rule.serialize_aws_json_1_0(
            value["rule"]
        )
    if "last_modified" in value:
        import aws_sdk_invoicing.types.last_modified_timestamp

        out["LastModified"] = (
            aws_sdk_invoicing.types.last_modified_timestamp.serialize_aws_json_1_0(
                value["last_modified"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceUnit:
    out: InvoiceUnit = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_invoicing.types.invoice_unit_rule

        out["rule"] = (
            aws_sdk_invoicing.types.invoice_unit_rule.deserialize_aws_json_1_0(
                data["Rule"]
            )
        )
    if "LastModified" in data:
        import aws_sdk_invoicing.types.last_modified_timestamp

        out["last_modified"] = (
            aws_sdk_invoicing.types.last_modified_timestamp.deserialize_aws_json_1_0(
                data["LastModified"]
            )
        )
    return out
