"""Generated from Smithy shape ``com.amazonaws.entityresolution#Schemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.schema_list

Schemas: TypeAlias = list["aws_sdk_entityresolution.types.schema_list.SchemaList"]


# --- restJson1 ser/de ---
def serialize_json(value: Schemas) -> list:
    import aws_sdk_entityresolution.types.schema_list

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.schema_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> Schemas:
    import aws_sdk_entityresolution.types.schema_list

    out: Schemas = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.schema_list.deserialize_json(item))
    return out
