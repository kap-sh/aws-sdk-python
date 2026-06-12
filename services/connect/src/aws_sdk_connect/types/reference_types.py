"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_type

ReferenceTypes: TypeAlias = list["aws_sdk_connect.types.reference_type.ReferenceType"]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceTypes) -> list:
    import aws_sdk_connect.types.reference_type

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.reference_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceTypes:
    import aws_sdk_connect.types.reference_type

    out: ReferenceTypes = []
    for item in data:
        out.append(aws_sdk_connect.types.reference_type.deserialize_json(item))
    return out
