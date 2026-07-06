"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateAccountsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id_list
    import aws_sdk_billingconductor.types.billing_group_arn


class AssociateAccountsInput(TypedDict, closed=True):
    arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>"""
    account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList"
    """<p> The associating array of account IDs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAccountsInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_billingconductor.types.account_id_list

    out["AccountIds"] = aws_sdk_billingconductor.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> AssociateAccountsInput:
    out: AssociateAccountsInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("AssociateAccountsInput.arn required")
    if "AccountIds" in data:
        import aws_sdk_billingconductor.types.account_id_list

        out["account_ids"] = (
            aws_sdk_billingconductor.types.account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        raise DeserializationError("AssociateAccountsInput.account_ids required")
    return out
