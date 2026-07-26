"""Generated from Smithy shape ``com.amazonaws.quicksight#RelationalTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.relational_table_catalog
    import capo_quicksight.types.relational_table_name
    import capo_quicksight.types.relational_table_schema


class RelationalTable(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the data source.</p>"""
    catalog: NotRequired[
        "capo_quicksight.types.relational_table_catalog.RelationalTableCatalog"
    ]
    """<p>The catalog associated with a table.</p>"""
    schema: NotRequired[
        "capo_quicksight.types.relational_table_schema.RelationalTableSchema"
    ]
    """<p>The schema name. This name applies to certain relational database engines.</p>"""
    name: "capo_quicksight.types.relational_table_name.RelationalTableName"
    """<p>The name of the relational table.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The column schema of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationalTable) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    out["Name"] = value["name"]
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> RelationalTable:
    out: RelationalTable = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("RelationalTable.data_source_arn required")
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Schema" in data:
        out["schema"] = data["Schema"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RelationalTable.name required")
    if "InputColumns" in data:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        raise DeserializationError("RelationalTable.input_columns required")
    return out
