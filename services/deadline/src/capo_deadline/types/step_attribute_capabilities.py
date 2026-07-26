"""Generated from Smithy shape ``com.amazonaws.deadline#StepAttributeCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.step_attribute_capability

StepAttributeCapabilities: TypeAlias = list[
    "capo_deadline.types.step_attribute_capability.StepAttributeCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepAttributeCapabilities) -> list:
    import capo_deadline.types.step_attribute_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.step_attribute_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepAttributeCapabilities:
    import capo_deadline.types.step_attribute_capability

    out: StepAttributeCapabilities = []
    for item in data:
        out.append(capo_deadline.types.step_attribute_capability.deserialize_json(item))
    return out
