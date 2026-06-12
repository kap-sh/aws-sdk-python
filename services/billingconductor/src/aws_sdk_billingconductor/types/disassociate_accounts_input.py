"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociateAccountsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id_list
    import aws_sdk_billingconductor.types.billing_group_arn


class DisassociateAccountsInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>"""
    account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList"
    """<p>The array of account IDs to disassociate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAccountsInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_billingconductor.types.account_id_list

    out["AccountIds"] = aws_sdk_billingconductor.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> DisassociateAccountsInput:
    out: DisassociateAccountsInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DisassociateAccountsInput.arn required")
    if "AccountIds" in data:
        import aws_sdk_billingconductor.types.account_id_list

        out["account_ids"] = (
            aws_sdk_billingconductor.types.account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        raise DeserializationError("DisassociateAccountsInput.account_ids required")
    return out
