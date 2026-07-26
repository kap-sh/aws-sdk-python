"""Generated from Smithy shape ``com.amazonaws.databrew#ExcelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.header_row
    import capo_databrew.types.sheet_index_list
    import capo_databrew.types.sheet_name_list


class ExcelOptions(TypedDict, closed=True):
    sheet_names: NotRequired["capo_databrew.types.sheet_name_list.SheetNameList"]
    """<p>One or more named sheets in the Excel file that will be included in the dataset.</p>"""
    sheet_indexes: NotRequired["capo_databrew.types.sheet_index_list.SheetIndexList"]
    """<p>One or more sheet numbers in the Excel file that will be included in the dataset.</p>"""
    header_row: NotRequired["capo_databrew.types.header_row.HeaderRow"]
    """<p>A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExcelOptions) -> dict:
    out: dict = {}
    if "sheet_names" in value:
        import capo_databrew.types.sheet_name_list

        out["SheetNames"] = capo_databrew.types.sheet_name_list.serialize_json(
            value["sheet_names"]
        )
    if "sheet_indexes" in value:
        import capo_databrew.types.sheet_index_list

        out["SheetIndexes"] = capo_databrew.types.sheet_index_list.serialize_json(
            value["sheet_indexes"]
        )
    if "header_row" in value:
        out["HeaderRow"] = value["header_row"]
    return out


def deserialize_json(data: dict) -> ExcelOptions:
    out: ExcelOptions = {}  # type: ignore[typeddict-item]
    if "SheetNames" in data:
        import capo_databrew.types.sheet_name_list

        out["sheet_names"] = capo_databrew.types.sheet_name_list.deserialize_json(
            data["SheetNames"]
        )
    if "SheetIndexes" in data:
        import capo_databrew.types.sheet_index_list

        out["sheet_indexes"] = capo_databrew.types.sheet_index_list.deserialize_json(
            data["SheetIndexes"]
        )
    if "HeaderRow" in data:
        out["header_row"] = data["HeaderRow"]
    return out
