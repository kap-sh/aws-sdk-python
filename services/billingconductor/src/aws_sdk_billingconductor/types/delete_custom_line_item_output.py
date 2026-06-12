"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeleteCustomLineItemOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn


class DeleteCustomLineItemOutput(TypedDict):
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p>The ARN of the deleted custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomLineItemOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteCustomLineItemOutput:
    out: DeleteCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
