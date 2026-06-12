"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_identifier

BatchGetFieldIdentifierList: TypeAlias = list[
    "aws_sdk_connectcases.types.field_identifier.FieldIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldIdentifierList) -> list:
    import aws_sdk_connectcases.types.field_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetFieldIdentifierList:
    import aws_sdk_connectcases.types.field_identifier

    out: BatchGetFieldIdentifierList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_identifier.deserialize_json(item))
    return out
