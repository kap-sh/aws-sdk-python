"""Generated from Smithy shape ``com.amazonaws.artifact#AgreementTerms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_artifact.types.long_string_attribute

AgreementTerms: TypeAlias = list[
    "aws_sdk_artifact.types.long_string_attribute.LongStringAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgreementTerms) -> list:
    return list(value)


def deserialize_json(data: list) -> AgreementTerms:
    return list(data)
