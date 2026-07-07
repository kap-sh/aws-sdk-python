"""Generated from Smithy shape ``com.amazonaws.quicksight#FontWeight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_weight_name


class FontWeight(TypedDict, closed=True):
    name: NotRequired["aws_sdk_quicksight.types.font_weight_name.FontWeightName"]
    """<p>The lexical name for the level of boldness of the text display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FontWeight) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_quicksight.types.font_weight_name

        out["Name"] = aws_sdk_quicksight.types.font_weight_name.serialize_json(
            value["name"]
        )
    return out


def deserialize_json(data: dict) -> FontWeight:
    out: FontWeight = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_quicksight.types.font_weight_name

        out["name"] = aws_sdk_quicksight.types.font_weight_name.deserialize_json(
            data["Name"]
        )
    return out
