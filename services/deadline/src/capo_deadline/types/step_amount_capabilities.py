"""Generated from Smithy shape ``com.amazonaws.deadline#StepAmountCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.step_amount_capability

StepAmountCapabilities: TypeAlias = list[
    "capo_deadline.types.step_amount_capability.StepAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepAmountCapabilities) -> list:
    import capo_deadline.types.step_amount_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.step_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepAmountCapabilities:
    import capo_deadline.types.step_amount_capability

    out: StepAmountCapabilities = []
    for item in data:
        out.append(capo_deadline.types.step_amount_capability.deserialize_json(item))
    return out
