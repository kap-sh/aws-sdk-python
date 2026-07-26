"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceThemeTypography``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.font_family


class WorkspaceThemeTypography(TypedDict, closed=True):
    font_family: NotRequired["capo_connect.types.font_family.FontFamily"]
    """<p>The font family configuration for text in the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceThemeTypography) -> dict:
    out: dict = {}
    if "font_family" in value:
        import capo_connect.types.font_family

        out["FontFamily"] = capo_connect.types.font_family.serialize_json(
            value["font_family"]
        )
    return out


def deserialize_json(data: dict) -> WorkspaceThemeTypography:
    out: WorkspaceThemeTypography = {}  # type: ignore[typeddict-item]
    if "FontFamily" in data:
        import capo_connect.types.font_family

        out["font_family"] = capo_connect.types.font_family.deserialize_json(
            data["FontFamily"]
        )
    return out
