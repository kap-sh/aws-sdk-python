"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageHeaderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.alignment


class InAppMessageHeaderConfig(TypedDict, closed=True):
    alignment: NotRequired["capo_pinpoint.types.alignment.Alignment"]
    """<p>The alignment of the text. Valid values: LEFT, CENTER, RIGHT.</p>"""
    header: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Message Header.</p>"""
    text_color: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The text color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageHeaderConfig) -> dict:
    out: dict = {}
    if "alignment" in value:
        import capo_pinpoint.types.alignment

        out["Alignment"] = capo_pinpoint.types.alignment.serialize_json(
            value["alignment"]
        )
    if "header" in value:
        out["Header"] = value["header"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> InAppMessageHeaderConfig:
    out: InAppMessageHeaderConfig = {}  # type: ignore[typeddict-item]
    if "Alignment" in data:
        import capo_pinpoint.types.alignment

        out["alignment"] = capo_pinpoint.types.alignment.deserialize_json(
            data["Alignment"]
        )
    if "Header" in data:
        out["header"] = data["Header"]
    if "TextColor" in data:
        out["text_color"] = data["TextColor"]
    return out
