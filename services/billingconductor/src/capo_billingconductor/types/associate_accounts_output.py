"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateAccountsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_arn


class AssociateAccountsOutput(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAccountsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AssociateAccountsOutput:
    out: AssociateAccountsOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
