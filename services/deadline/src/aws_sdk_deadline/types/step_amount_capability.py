"""Generated from Smithy shape ``com.amazonaws.deadline#StepAmountCapability``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.amount_capability_name
    import aws_sdk_deadline.types.double


class StepAmountCapability(TypedDict):
    name: "aws_sdk_deadline.types.amount_capability_name.AmountCapabilityName"
    """<p>The name of the step.</p>"""
    min: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The minimum amount.</p>"""
    max: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The maximum amount.</p>"""
    value: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The amount value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StepAmountCapability:
    out: StepAmountCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StepAmountCapability.name required")
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    if "value" in data:
        out["value"] = data["value"]
    return out
