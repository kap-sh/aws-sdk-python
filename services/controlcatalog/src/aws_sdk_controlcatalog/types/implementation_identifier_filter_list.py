"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationIdentifierFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.implementation_identifier

ImplementationIdentifierFilterList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.implementation_identifier.ImplementationIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationIdentifierFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ImplementationIdentifierFilterList:
    return list(data)
