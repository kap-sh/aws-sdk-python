"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.scalar_type


class ColumnType(TypedDict):
    scalar_type: NotRequired["aws_sdk_iotsitewise.types.scalar_type.ScalarType"]
    """<p>The allowed data types that the column has as it's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnType) -> dict:
    out: dict = {}
    if "scalar_type" in value:
        import aws_sdk_iotsitewise.types.scalar_type

        out["scalarType"] = aws_sdk_iotsitewise.types.scalar_type.serialize_json(
            value["scalar_type"]
        )
    return out


def deserialize_json(data: dict) -> ColumnType:
    out: ColumnType = {}  # type: ignore[typeddict-item]
    if "scalarType" in data:
        import aws_sdk_iotsitewise.types.scalar_type

        out["scalar_type"] = aws_sdk_iotsitewise.types.scalar_type.deserialize_json(
            data["scalarType"]
        )
    return out
