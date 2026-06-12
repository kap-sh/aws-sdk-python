"""Generated from Smithy shape ``com.amazonaws.iot#PolicyDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_document

PolicyDocuments: TypeAlias = list["aws_sdk_iot.types.policy_document.PolicyDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDocuments) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyDocuments:
    return list(data)
