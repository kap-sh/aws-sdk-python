"""Generated from Smithy shape ``com.amazonaws.keyspaces#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.field_definition

FieldList: TypeAlias = list["capo_keyspaces.types.field_definition.FieldDefinition"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldList) -> list:
    import capo_keyspaces.types.field_definition

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.field_definition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FieldList:
    import capo_keyspaces.types.field_definition

    out: FieldList = []
    for item in data:
        out.append(capo_keyspaces.types.field_definition.deserialize_aws_json_1_0(item))
    return out
