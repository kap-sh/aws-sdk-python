"""Generated from Smithy shape ``com.amazonaws.datazone#ColumnFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.column_name_list


class ColumnFilterConfiguration(TypedDict, closed=True):
    included_column_names: NotRequired[
        "capo_datazone.types.column_name_list.ColumnNameList"
    ]
    """<p>Specifies whether to include column names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnFilterConfiguration) -> dict:
    out: dict = {}
    if "included_column_names" in value:
        import capo_datazone.types.column_name_list

        out["includedColumnNames"] = (
            capo_datazone.types.column_name_list.serialize_json(
                value["included_column_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnFilterConfiguration:
    out: ColumnFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "includedColumnNames" in data:
        import capo_datazone.types.column_name_list

        out["included_column_names"] = (
            capo_datazone.types.column_name_list.deserialize_json(
                data["includedColumnNames"]
            )
        )
    return out
