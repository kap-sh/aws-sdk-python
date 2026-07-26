"""Generated from Smithy shape ``com.amazonaws.quicksight#SaaSTable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.table_path_element_list


class SaaSTable(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the SaaS data source.</p>"""
    table_path: "capo_quicksight.types.table_path_element_list.TablePathElementList"
    """<p>The hierarchical path to the table within the SaaS data source.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The list of input columns available from the SaaS table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSTable) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    import capo_quicksight.types.table_path_element_list

    out["TablePath"] = capo_quicksight.types.table_path_element_list.serialize_json(
        value["table_path"]
    )
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> SaaSTable:
    out: SaaSTable = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("SaaSTable.data_source_arn required")
    if "TablePath" in data:
        import capo_quicksight.types.table_path_element_list

        out["table_path"] = (
            capo_quicksight.types.table_path_element_list.deserialize_json(
                data["TablePath"]
            )
        )
    else:
        raise DeserializationError("SaaSTable.table_path required")
    if "InputColumns" in data:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        raise DeserializationError("SaaSTable.input_columns required")
    return out
