"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialNullDataSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_null_symbol_style


class GeospatialNullDataSettings(TypedDict):
    symbol_style: "aws_sdk_quicksight.types.geospatial_null_symbol_style.GeospatialNullSymbolStyle"
    """<p>The symbol style for null data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialNullDataSettings) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.geospatial_null_symbol_style

    out["SymbolStyle"] = (
        aws_sdk_quicksight.types.geospatial_null_symbol_style.serialize_json(
            value["symbol_style"]
        )
    )
    return out


def deserialize_json(data: dict) -> GeospatialNullDataSettings:
    out: GeospatialNullDataSettings = {}  # type: ignore[typeddict-item]
    if "SymbolStyle" in data:
        import aws_sdk_quicksight.types.geospatial_null_symbol_style

        out["symbol_style"] = (
            aws_sdk_quicksight.types.geospatial_null_symbol_style.deserialize_json(
                data["SymbolStyle"]
            )
        )
    else:
        raise DeserializationError("GeospatialNullDataSettings.symbol_style required")
    return out
