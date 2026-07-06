"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerAmountCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.amount_capability_name


class WorkerAmountCapability(TypedDict, closed=True):
    name: "aws_sdk_deadline.types.amount_capability_name.AmountCapabilityName"
    """<p>The name of the worker amount capability.</p>"""
    value: "float"
    """<p>The value of the worker amount capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> WorkerAmountCapability:
    out: WorkerAmountCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkerAmountCapability.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("WorkerAmountCapability.value required")
    return out
