"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociateAccountsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn


class DisassociateAccountsOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs is disassociated from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAccountsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DisassociateAccountsOutput:
    out: DisassociateAccountsOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
