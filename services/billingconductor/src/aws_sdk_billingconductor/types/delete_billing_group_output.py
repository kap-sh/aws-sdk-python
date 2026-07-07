"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeleteBillingGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn


class DeleteBillingGroupOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the deleted billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBillingGroupOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteBillingGroupOutput:
    out: DeleteBillingGroupOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
