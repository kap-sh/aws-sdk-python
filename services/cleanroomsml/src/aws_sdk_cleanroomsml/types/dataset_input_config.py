"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetInputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.data_source
    import aws_sdk_cleanroomsml.types.dataset_schema_list


class DatasetInputConfig(TypedDict):
    schema: "aws_sdk_cleanroomsml.types.dataset_schema_list.DatasetSchemaList"
    """<p>The schema information for the training data.</p>"""
    data_source: "aws_sdk_cleanroomsml.types.data_source.DataSource"
    """<p>A DataSource object that specifies the Glue data source for the training data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetInputConfig) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.dataset_schema_list

    out["schema"] = aws_sdk_cleanroomsml.types.dataset_schema_list.serialize_json(
        value["schema"]
    )
    import aws_sdk_cleanroomsml.types.data_source

    out["dataSource"] = aws_sdk_cleanroomsml.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> DatasetInputConfig:
    out: DatasetInputConfig = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_cleanroomsml.types.dataset_schema_list

        out["schema"] = aws_sdk_cleanroomsml.types.dataset_schema_list.deserialize_json(
            data["schema"]
        )
    else:
        raise DeserializationError("DatasetInputConfig.schema required")
    if "dataSource" in data:
        import aws_sdk_cleanroomsml.types.data_source

        out["data_source"] = aws_sdk_cleanroomsml.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("DatasetInputConfig.data_source required")
    return out
