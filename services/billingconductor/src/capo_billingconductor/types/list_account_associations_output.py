"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListAccountAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_associations_list
    import capo_billingconductor.types.token


class ListAccountAssociationsOutput(TypedDict, closed=True):
    linked_accounts: NotRequired[
        "capo_billingconductor.types.account_associations_list.AccountAssociationsList"
    ]
    """<p> The list of linked accounts in the payer account. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get accounts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsOutput) -> dict:
    out: dict = {}
    if "linked_accounts" in value:
        import capo_billingconductor.types.account_associations_list

        out["LinkedAccounts"] = (
            capo_billingconductor.types.account_associations_list.serialize_json(
                value["linked_accounts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsOutput:
    out: ListAccountAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "LinkedAccounts" in data:
        import capo_billingconductor.types.account_associations_list

        out["linked_accounts"] = (
            capo_billingconductor.types.account_associations_list.deserialize_json(
                data["LinkedAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
