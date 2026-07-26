"""Generated from Smithy shape ``com.amazonaws.iot#PolicyDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.policy_document

PolicyDocuments: TypeAlias = list["capo_iot.types.policy_document.PolicyDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDocuments) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyDocuments:
    return list(data)
