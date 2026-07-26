"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelFieldTypeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.string

DataSourceIntrospectionModelFieldTypeValues: TypeAlias = list[
    "capo_appsync.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelFieldTypeValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSourceIntrospectionModelFieldTypeValues:
    return list(data)
