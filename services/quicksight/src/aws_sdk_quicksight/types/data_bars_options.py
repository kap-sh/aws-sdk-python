"""Generated from Smithy shape ``com.amazonaws.quicksight#DataBarsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.hex_color


class DataBarsOptions(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID for the data bars options.</p>"""
    positive_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the positive data bar.</p>"""
    negative_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the negative data bar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataBarsOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "positive_color" in value:
        out["PositiveColor"] = value["positive_color"]
    if "negative_color" in value:
        out["NegativeColor"] = value["negative_color"]
    return out


def deserialize_json(data: dict) -> DataBarsOptions:
    out: DataBarsOptions = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DataBarsOptions.field_id required")
    if "PositiveColor" in data:
        out["positive_color"] = data["PositiveColor"]
    if "NegativeColor" in data:
        out["negative_color"] = data["NegativeColor"]
    return out
