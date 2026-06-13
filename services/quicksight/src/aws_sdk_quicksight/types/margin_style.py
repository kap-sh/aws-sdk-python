"""Generated from Smithy shape ``com.amazonaws.quicksight#MarginStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class MarginStyle(TypedDict):
    show: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>This Boolean value controls whether to display sheet margins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarginStyle) -> dict:
    out: dict = {}
    if "show" in value:
        out["Show"] = value["show"]
    return out


def deserialize_json(data: dict) -> MarginStyle:
    out: MarginStyle = {}  # type: ignore[typeddict-item]
    if "Show" in data:
        out["show"] = data["Show"]
    return out
