"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.scalar_type


class ColumnType(TypedDict, closed=True):
    scalar_type: NotRequired["capo_iotsitewise.types.scalar_type.ScalarType"]
    """<p>The allowed data types that the column has as it's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnType) -> dict:
    out: dict = {}
    if "scalar_type" in value:
        import capo_iotsitewise.types.scalar_type

        out["scalarType"] = capo_iotsitewise.types.scalar_type.serialize_json(
            value["scalar_type"]
        )
    return out


def deserialize_json(data: dict) -> ColumnType:
    out: ColumnType = {}  # type: ignore[typeddict-item]
    if "scalarType" in data:
        import capo_iotsitewise.types.scalar_type

        out["scalar_type"] = capo_iotsitewise.types.scalar_type.deserialize_json(
            data["scalarType"]
        )
    return out
