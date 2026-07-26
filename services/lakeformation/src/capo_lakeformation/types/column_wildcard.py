"""Generated from Smithy shape ``com.amazonaws.lakeformation#ColumnWildcard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.column_names


class ColumnWildcard(TypedDict, closed=True):
    excluded_column_names: NotRequired[
        "capo_lakeformation.types.column_names.ColumnNames"
    ]
    """<p>Excludes column names. Any column with this name will be excluded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnWildcard) -> dict:
    out: dict = {}
    if "excluded_column_names" in value:
        import capo_lakeformation.types.column_names

        out["ExcludedColumnNames"] = (
            capo_lakeformation.types.column_names.serialize_json(
                value["excluded_column_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnWildcard:
    out: ColumnWildcard = {}  # type: ignore[typeddict-item]
    if "ExcludedColumnNames" in data:
        import capo_lakeformation.types.column_names

        out["excluded_column_names"] = (
            capo_lakeformation.types.column_names.deserialize_json(
                data["ExcludedColumnNames"]
            )
        )
    return out
