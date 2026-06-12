"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.column_type
    import aws_sdk_iotsitewise.types.string


class ColumnInfo(TypedDict):
    name: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The name of the column description.</p>"""
    type: NotRequired["aws_sdk_iotsitewise.types.column_type.ColumnType"]
    """<p>The type of the column description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_iotsitewise.types.column_type

        out["type"] = aws_sdk_iotsitewise.types.column_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> ColumnInfo:
    out: ColumnInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_iotsitewise.types.column_type

        out["type"] = aws_sdk_iotsitewise.types.column_type.deserialize_json(
            data["type"]
        )
    return out
