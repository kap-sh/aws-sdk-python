"""Generated from Smithy shape ``com.amazonaws.braket#HybridJobAdditionalAttributeNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.hybrid_job_additional_attribute_name

HybridJobAdditionalAttributeNamesList: TypeAlias = list[
    "aws_sdk_braket.types.hybrid_job_additional_attribute_name.HybridJobAdditionalAttributeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: HybridJobAdditionalAttributeNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> HybridJobAdditionalAttributeNamesList:
    return list(data)
