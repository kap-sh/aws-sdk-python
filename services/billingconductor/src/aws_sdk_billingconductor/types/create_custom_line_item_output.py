"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreateCustomLineItemOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn


class CreateCustomLineItemOutput(TypedDict):
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the created custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomLineItemOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateCustomLineItemOutput:
    out: CreateCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
