"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.row_filter


class RowFilterConfiguration(TypedDict):
    row_filter: "aws_sdk_datazone.types.row_filter.RowFilter"
    """<p>The row filter.</p>"""
    sensitive: "bool"
    """<p>Specifies whether the row filter is sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowFilterConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.row_filter

    out["rowFilter"] = aws_sdk_datazone.types.row_filter.serialize_json(
        value["row_filter"]
    )
    out["sensitive"] = value.get("sensitive", True)
    return out


def deserialize_json(data: dict) -> RowFilterConfiguration:
    out: RowFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "rowFilter" in data:
        import aws_sdk_datazone.types.row_filter

        out["row_filter"] = aws_sdk_datazone.types.row_filter.deserialize_json(
            data["rowFilter"]
        )
    else:
        raise DeserializationError("RowFilterConfiguration.row_filter required")
    if "sensitive" in data:
        out["sensitive"] = data["sensitive"]
    else:
        out["sensitive"] = True
    return out
