"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingGroupAccountGrouping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.responsibility_transfer_arn


class UpdateBillingGroupAccountGrouping(TypedDict):
    auto_associate: NotRequired["bool"]
    """<p>Specifies if this billing group will automatically associate newly added Amazon Web Services accounts that join your consolidated billing family.</p>"""
    responsibility_transfer_arn: NotRequired[
        "aws_sdk_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    ]
    """<p> The Amazon Resource Name (ARN) that identifies the transfer relationship. Note: Modifications to the ResponsibilityTransferArn are not permitted for existing billing groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupAccountGrouping) -> dict:
    out: dict = {}
    if "auto_associate" in value:
        out["AutoAssociate"] = value["auto_associate"]
    if "responsibility_transfer_arn" in value:
        out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupAccountGrouping:
    out: UpdateBillingGroupAccountGrouping = {}  # type: ignore[typeddict-item]
    if "AutoAssociate" in data:
        out["auto_associate"] = data["AutoAssociate"]
    if "ResponsibilityTransferArn" in data:
        out["responsibility_transfer_arn"] = data["ResponsibilityTransferArn"]
    return out
