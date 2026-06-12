"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeleteBillingGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn


class DeleteBillingGroupInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBillingGroupInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteBillingGroupInput:
    out: DeleteBillingGroupInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeleteBillingGroupInput.arn required")
    return out
