"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DataSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.glue_data_source


class DataSource(TypedDict):
    glue_data_source: "aws_sdk_cleanroomsml.types.glue_data_source.GlueDataSource"
    """<p>A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.glue_data_source

    out["glueDataSource"] = aws_sdk_cleanroomsml.types.glue_data_source.serialize_json(
        value["glue_data_source"]
    )
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "glueDataSource" in data:
        import aws_sdk_cleanroomsml.types.glue_data_source

        out["glue_data_source"] = (
            aws_sdk_cleanroomsml.types.glue_data_source.deserialize_json(
                data["glueDataSource"]
            )
        )
    else:
        raise DeserializationError("DataSource.glue_data_source required")
    return out
