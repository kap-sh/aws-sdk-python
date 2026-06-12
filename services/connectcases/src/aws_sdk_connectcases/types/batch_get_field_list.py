"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.get_field_response

BatchGetFieldList: TypeAlias = list[
    "aws_sdk_connectcases.types.get_field_response.GetFieldResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldList) -> list:
    import aws_sdk_connectcases.types.get_field_response

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.get_field_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetFieldList:
    import aws_sdk_connectcases.types.get_field_response

    out: BatchGetFieldList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.get_field_response.deserialize_json(item))
    return out
