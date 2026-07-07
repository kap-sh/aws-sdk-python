"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupAccountGrouping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.responsibility_transfer_arn


class ListBillingGroupAccountGrouping(TypedDict, closed=True):
    auto_associate: NotRequired["bool"]
    """<p>Specifies if this billing group will automatically associate newly added Amazon Web Services accounts that join your consolidated billing family.</p>"""
    responsibility_transfer_arn: NotRequired[
        "aws_sdk_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    ]
    """<p> The Amazon Resource Name (ARN) that identifies the transfer relationship for the billing group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupAccountGrouping) -> dict:
    out: dict = {}
    if "auto_associate" in value:
        out["AutoAssociate"] = value["auto_associate"]
    if "responsibility_transfer_arn" in value:
        out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupAccountGrouping:
    out: ListBillingGroupAccountGrouping = {}  # type: ignore[typeddict-item]
    if "AutoAssociate" in data:
        out["auto_associate"] = data["AutoAssociate"]
    if "ResponsibilityTransferArn" in data:
        out["responsibility_transfer_arn"] = data["ResponsibilityTransferArn"]
    return out
