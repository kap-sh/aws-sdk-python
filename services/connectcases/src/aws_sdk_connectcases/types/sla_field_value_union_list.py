"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaFieldValueUnionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value_union

SlaFieldValueUnionList: TypeAlias = list[
    "aws_sdk_connectcases.types.field_value_union.FieldValueUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlaFieldValueUnionList) -> list:
    import aws_sdk_connectcases.types.field_value_union

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_value_union.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlaFieldValueUnionList:
    import aws_sdk_connectcases.types.field_value_union

    out: SlaFieldValueUnionList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_value_union.deserialize_json(item))
    return out
