"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelIndexFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.string

DataSourceIntrospectionModelIndexFields: TypeAlias = list[
    "capo_appsync.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelIndexFields) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSourceIntrospectionModelIndexFields:
    return list(data)
