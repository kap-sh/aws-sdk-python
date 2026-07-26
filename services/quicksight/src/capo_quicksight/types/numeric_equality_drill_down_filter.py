"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericEqualityDrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.double


class NumericEqualityDrillDownFilter(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    value: "capo_quicksight.types.double.Double"
    """<p>The value of the double input numeric drill down filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericEqualityDrillDownFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> NumericEqualityDrillDownFilter:
    out: NumericEqualityDrillDownFilter = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NumericEqualityDrillDownFilter.column required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out
