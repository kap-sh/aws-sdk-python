"""Generated from Smithy shape ``com.amazonaws.billingconductor#AccountGrouping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id_list
    import capo_billingconductor.types.responsibility_transfer_arn


class AccountGrouping(TypedDict, closed=True):
    linked_account_ids: "capo_billingconductor.types.account_id_list.AccountIdList"
    """<p>The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.</p>"""
    auto_associate: NotRequired["bool"]
    """<p>Specifies if this billing group will automatically associate newly added Amazon Web Services accounts that join your consolidated billing family.</p>"""
    responsibility_transfer_arn: NotRequired[
        "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    ]
    """<p> The Amazon Resource Name (ARN) that identifies the transfer relationship owned by the Bill Transfer account (caller account). When specified, the PrimaryAccountId is no longer required. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountGrouping) -> dict:
    out: dict = {}
    import capo_billingconductor.types.account_id_list

    out["LinkedAccountIds"] = (
        capo_billingconductor.types.account_id_list.serialize_json(
            value.get("linked_account_ids", [])
        )
    )
    if "auto_associate" in value:
        out["AutoAssociate"] = value["auto_associate"]
    if "responsibility_transfer_arn" in value:
        out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    return out


def deserialize_json(data: dict) -> AccountGrouping:
    out: AccountGrouping = {}  # type: ignore[typeddict-item]
    if "LinkedAccountIds" in data:
        import capo_billingconductor.types.account_id_list

        out["linked_account_ids"] = (
            capo_billingconductor.types.account_id_list.deserialize_json(
                data["LinkedAccountIds"]
            )
        )
    else:
        out["linked_account_ids"] = []
    if "AutoAssociate" in data:
        out["auto_associate"] = data["AutoAssociate"]
    if "ResponsibilityTransferArn" in data:
        out["responsibility_transfer_arn"] = data["ResponsibilityTransferArn"]
    return out
