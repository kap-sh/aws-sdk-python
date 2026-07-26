"""Generated from Smithy shape ``com.amazonaws.connect#FontFamily``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.workspace_font_family


class FontFamily(TypedDict, closed=True):
    default: NotRequired["capo_connect.types.workspace_font_family.WorkspaceFontFamily"]
    """<p>The default font family to use in the workspace theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FontFamily) -> dict:
    out: dict = {}
    if "default" in value:
        import capo_connect.types.workspace_font_family

        out["Default"] = capo_connect.types.workspace_font_family.serialize_json(
            value["default"]
        )
    return out


def deserialize_json(data: dict) -> FontFamily:
    out: FontFamily = {}  # type: ignore[typeddict-item]
    if "Default" in data:
        import capo_connect.types.workspace_font_family

        out["default"] = capo_connect.types.workspace_font_family.deserialize_json(
            data["Default"]
        )
    return out
