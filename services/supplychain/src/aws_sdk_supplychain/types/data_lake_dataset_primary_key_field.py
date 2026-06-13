"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPrimaryKeyField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field_name


class DataLakeDatasetPrimaryKeyField(TypedDict):
    name: "aws_sdk_supplychain.types.data_lake_dataset_schema_field_name.DataLakeDatasetSchemaFieldName"
    """<p>The name of the primary key field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPrimaryKeyField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DataLakeDatasetPrimaryKeyField:
    out: DataLakeDatasetPrimaryKeyField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataLakeDatasetPrimaryKeyField.name required")
    return out
