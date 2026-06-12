"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListAccountAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_associations_list
    import aws_sdk_billingconductor.types.token


class ListAccountAssociationsOutput(TypedDict):
    linked_accounts: NotRequired[
        "aws_sdk_billingconductor.types.account_associations_list.AccountAssociationsList"
    ]
    """<p> The list of linked accounts in the payer account. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get accounts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsOutput) -> dict:
    out: dict = {}
    if "linked_accounts" in value:
        import aws_sdk_billingconductor.types.account_associations_list

        out["LinkedAccounts"] = (
            aws_sdk_billingconductor.types.account_associations_list.serialize_json(
                value["linked_accounts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsOutput:
    out: ListAccountAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "LinkedAccounts" in data:
        import aws_sdk_billingconductor.types.account_associations_list

        out["linked_accounts"] = (
            aws_sdk_billingconductor.types.account_associations_list.deserialize_json(
                data["LinkedAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
