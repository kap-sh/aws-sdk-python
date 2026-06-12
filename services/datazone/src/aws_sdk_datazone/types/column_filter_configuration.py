"""Generated from Smithy shape ``com.amazonaws.datazone#ColumnFilterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.column_name_list

class ColumnFilterConfiguration(TypedDict):
    included_column_names: NotRequired["aws_sdk_datazone.types.column_name_list.ColumnNameList"]
    """<p>Specifies whether to include column names.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ColumnFilterConfiguration) -> dict:
    out: dict = {}
    if "included_column_names" in value:
        import aws_sdk_datazone.types.column_name_list
        out["includedColumnNames"] = aws_sdk_datazone.types.column_name_list.serialize_json(value["included_column_names"])
    return out


def deserialize_json(data: dict) -> ColumnFilterConfiguration:
    out: ColumnFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "includedColumnNames" in data:
        import aws_sdk_datazone.types.column_name_list
        out["included_column_names"] = aws_sdk_datazone.types.column_name_list.deserialize_json(data["includedColumnNames"])
    return out