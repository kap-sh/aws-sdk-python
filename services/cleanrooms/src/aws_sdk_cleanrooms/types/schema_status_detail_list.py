"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.schema_status_detail

SchemaStatusDetailList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.schema_status_detail.SchemaStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusDetailList) -> list:
    import aws_sdk_cleanrooms.types.schema_status_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.schema_status_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaStatusDetailList:
    import aws_sdk_cleanrooms.types.schema_status_detail

    out: SchemaStatusDetailList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.schema_status_detail.deserialize_json(item))
    return out
