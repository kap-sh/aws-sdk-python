"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetTooltip``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class SheetTooltip(TypedDict, closed=True):
    sheet_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The sheet ID of the tooltip sheet that is used by the tooltip.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetTooltip) -> dict:
    out: dict = {}
    if "sheet_id" in value:
        out["SheetId"] = value["sheet_id"]
    return out


def deserialize_json(data: dict) -> SheetTooltip:
    out: SheetTooltip = {}  # type: ignore[typeddict-item]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    return out
