"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field_name
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field_type


class DataLakeDatasetSchemaField(TypedDict, closed=True):
    name: "aws_sdk_supplychain.types.data_lake_dataset_schema_field_name.DataLakeDatasetSchemaFieldName"
    """<p>The dataset field name.</p>"""
    type: "aws_sdk_supplychain.types.data_lake_dataset_schema_field_type.DataLakeDatasetSchemaFieldType"
    """<p>The dataset field type.</p>"""
    is_required: "bool"
    """<p>Indicate if the field is required or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchemaField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field_type

    out["type"] = (
        aws_sdk_supplychain.types.data_lake_dataset_schema_field_type.serialize_json(
            value["type"]
        )
    )
    out["isRequired"] = value["is_required"]
    return out


def deserialize_json(data: dict) -> DataLakeDatasetSchemaField:
    out: DataLakeDatasetSchemaField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataLakeDatasetSchemaField.name required")
    if "type" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_schema_field_type

        out["type"] = (
            aws_sdk_supplychain.types.data_lake_dataset_schema_field_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DataLakeDatasetSchemaField.type required")
    if "isRequired" in data:
        out["is_required"] = data["isRequired"]
    else:
        raise DeserializationError("DataLakeDatasetSchemaField.is_required required")
    return out
