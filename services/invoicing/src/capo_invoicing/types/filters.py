"""Generated from Smithy shape ``com.amazonaws.invoicing#Filters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_list
    import capo_invoicing.types.invoice_unit_names


class Filters(TypedDict, closed=True):
    names: NotRequired["capo_invoicing.types.invoice_unit_names.InvoiceUnitNames"]
    """<p> An optional input to the list API. You can specify a list of invoice unit names inside filters to return invoice units that match only the specified invoice unit names. If multiple names are provided, the result is an <code>OR</code> condition (match any) of the specified invoice unit names. </p>"""
    invoice_receivers: NotRequired["capo_invoicing.types.account_id_list.AccountIdList"]
    """<p> You can specify a list of Amazon Web Services account IDs inside filters to return invoice units that match only the specified accounts. If multiple accounts are provided, the result is an <code>OR</code> condition (match any) of the specified accounts. This filter only matches the specified accounts on the invoice receivers of the invoice units. </p>"""
    accounts: NotRequired["capo_invoicing.types.account_id_list.AccountIdList"]
    """<p> You can specify a list of Amazon Web Services account IDs inside filters to return invoice units that match only the specified accounts. If multiple accounts are provided, the result is an <code>OR</code> condition (match any) of the specified accounts. The specified account IDs are matched with either the receiver or the linked accounts in the rules. </p>"""
    bill_source_accounts: NotRequired[
        "capo_invoicing.types.account_id_list.AccountIdList"
    ]
    """<p> A list of Amazon Web Services account IDs used to filter invoice units. These are payer accounts from other Organizations that have delegated their billing responsibility to the receiver account through the billing transfer feature. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filters) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_invoicing.types.invoice_unit_names

        out["Names"] = capo_invoicing.types.invoice_unit_names.serialize_aws_json_1_0(
            value["names"]
        )
    if "invoice_receivers" in value:
        import capo_invoicing.types.account_id_list

        out["InvoiceReceivers"] = (
            capo_invoicing.types.account_id_list.serialize_aws_json_1_0(
                value["invoice_receivers"]
            )
        )
    if "accounts" in value:
        import capo_invoicing.types.account_id_list

        out["Accounts"] = capo_invoicing.types.account_id_list.serialize_aws_json_1_0(
            value["accounts"]
        )
    if "bill_source_accounts" in value:
        import capo_invoicing.types.account_id_list

        out["BillSourceAccounts"] = (
            capo_invoicing.types.account_id_list.serialize_aws_json_1_0(
                value["bill_source_accounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Filters:
    out: Filters = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import capo_invoicing.types.invoice_unit_names

        out["names"] = capo_invoicing.types.invoice_unit_names.deserialize_aws_json_1_0(
            data["Names"]
        )
    if "InvoiceReceivers" in data:
        import capo_invoicing.types.account_id_list

        out["invoice_receivers"] = (
            capo_invoicing.types.account_id_list.deserialize_aws_json_1_0(
                data["InvoiceReceivers"]
            )
        )
    if "Accounts" in data:
        import capo_invoicing.types.account_id_list

        out["accounts"] = capo_invoicing.types.account_id_list.deserialize_aws_json_1_0(
            data["Accounts"]
        )
    if "BillSourceAccounts" in data:
        import capo_invoicing.types.account_id_list

        out["bill_source_accounts"] = (
            capo_invoicing.types.account_id_list.deserialize_aws_json_1_0(
                data["BillSourceAccounts"]
            )
        )
    return out
