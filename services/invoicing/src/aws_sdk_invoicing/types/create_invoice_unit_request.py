"""Generated from Smithy shape ``com.amazonaws.invoicing#CreateInvoiceUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_string
    import aws_sdk_invoicing.types.basic_string_without_space
    import aws_sdk_invoicing.types.description_string
    import aws_sdk_invoicing.types.invoice_unit_name
    import aws_sdk_invoicing.types.invoice_unit_rule
    import aws_sdk_invoicing.types.resource_tag_list
    import aws_sdk_invoicing.types.tax_inheritance_disabled_flag


class CreateInvoiceUnitRequest(TypedDict, closed=True):
    name: "aws_sdk_invoicing.types.invoice_unit_name.InvoiceUnitName"
    """<p> The unique name of the invoice unit that is shown on the generated invoice. This can't be changed once it is set. To change this name, you must delete the invoice unit recreate. </p>"""
    invoice_receiver: "aws_sdk_invoicing.types.account_id_string.AccountIdString"
    """<p> The Amazon Web Services account ID chosen to be the receiver of an invoice unit. All invoices generated for that invoice unit will be sent to this account ID. </p>"""
    description: NotRequired[
        "aws_sdk_invoicing.types.description_string.DescriptionString"
    ]
    """<p> The invoice unit's description. This can be changed at a later time. </p>"""
    tax_inheritance_disabled: "aws_sdk_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
    """<p>Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>"""
    rule: "aws_sdk_invoicing.types.invoice_unit_rule.InvoiceUnitRule"
    """<p>The <code>InvoiceUnitRule</code> object used to create invoice units. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_invoicing.types.resource_tag_list.ResourceTagList"
    ]
    """<p> The tag structure that contains a tag key and value. </p>"""
    client_token: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateInvoiceUnitRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["InvoiceReceiver"] = value["invoice_receiver"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TaxInheritanceDisabled"] = value.get("tax_inheritance_disabled", False)
    import aws_sdk_invoicing.types.invoice_unit_rule

    out["Rule"] = aws_sdk_invoicing.types.invoice_unit_rule.serialize_aws_json_1_0(
        value["rule"]
    )
    if "resource_tags" in value:
        import aws_sdk_invoicing.types.resource_tag_list

        out["ResourceTags"] = (
            aws_sdk_invoicing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateInvoiceUnitRequest:
    out: CreateInvoiceUnitRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateInvoiceUnitRequest.name required")
    if "InvoiceReceiver" in data:
        out["invoice_receiver"] = data["InvoiceReceiver"]
    else:
        raise DeserializationError("CreateInvoiceUnitRequest.invoice_receiver required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "TaxInheritanceDisabled" in data:
        out["tax_inheritance_disabled"] = data["TaxInheritanceDisabled"]
    else:
        out["tax_inheritance_disabled"] = False
    if "Rule" in data:
        import aws_sdk_invoicing.types.invoice_unit_rule

        out["rule"] = (
            aws_sdk_invoicing.types.invoice_unit_rule.deserialize_aws_json_1_0(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError("CreateInvoiceUnitRequest.rule required")
    if "ResourceTags" in data:
        import aws_sdk_invoicing.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_invoicing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["ResourceTags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
