"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceUnitRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.rule_account_id_list


class InvoiceUnitRule(TypedDict, closed=True):
    linked_accounts: NotRequired[
        "aws_sdk_invoicing.types.rule_account_id_list.RuleAccountIdList"
    ]
    """<p>The list of <code>LINKED_ACCOUNT</code> IDs where charges are included within the invoice unit. </p>"""
    bill_source_accounts: NotRequired[
        "aws_sdk_invoicing.types.rule_account_id_list.RuleAccountIdList"
    ]
    """<p> A list of Amazon Web Services account IDs that have delegated their billing responsibility to the receiver account through transfer billing. Unlike linked accounts, these bill source accounts can be payer accounts from other organizations that have authorized billing transfer to this account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceUnitRule) -> dict:
    out: dict = {}
    if "linked_accounts" in value:
        import aws_sdk_invoicing.types.rule_account_id_list

        out["LinkedAccounts"] = (
            aws_sdk_invoicing.types.rule_account_id_list.serialize_aws_json_1_0(
                value["linked_accounts"]
            )
        )
    if "bill_source_accounts" in value:
        import aws_sdk_invoicing.types.rule_account_id_list

        out["BillSourceAccounts"] = (
            aws_sdk_invoicing.types.rule_account_id_list.serialize_aws_json_1_0(
                value["bill_source_accounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceUnitRule:
    out: InvoiceUnitRule = {}  # type: ignore[typeddict-item]
    if "LinkedAccounts" in data:
        import aws_sdk_invoicing.types.rule_account_id_list

        out["linked_accounts"] = (
            aws_sdk_invoicing.types.rule_account_id_list.deserialize_aws_json_1_0(
                data["LinkedAccounts"]
            )
        )
    if "BillSourceAccounts" in data:
        import aws_sdk_invoicing.types.rule_account_id_list

        out["bill_source_accounts"] = (
            aws_sdk_invoicing.types.rule_account_id_list.deserialize_aws_json_1_0(
                data["BillSourceAccounts"]
            )
        )
    return out
