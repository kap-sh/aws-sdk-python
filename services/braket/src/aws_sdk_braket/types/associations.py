"""Generated from Smithy shape ``com.amazonaws.braket#Associations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.association

Associations: TypeAlias = list["aws_sdk_braket.types.association.Association"]


# --- restJson1 ser/de ---
def serialize_json(value: Associations) -> list:
    import aws_sdk_braket.types.association

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.association.serialize_json(item))
    return out


def deserialize_json(data: list) -> Associations:
    import aws_sdk_braket.types.association

    out: Associations = []
    for item in data:
        out.append(aws_sdk_braket.types.association.deserialize_json(item))
    return out
