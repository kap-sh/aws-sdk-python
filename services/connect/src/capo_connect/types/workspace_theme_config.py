"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceThemeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.workspace_theme_images
    import capo_connect.types.workspace_theme_palette
    import capo_connect.types.workspace_theme_typography


class WorkspaceThemeConfig(TypedDict, closed=True):
    palette: NotRequired[
        "capo_connect.types.workspace_theme_palette.WorkspaceThemePalette"
    ]
    """<p>The color palette configuration for the workspace theme.</p>"""
    images: NotRequired[
        "capo_connect.types.workspace_theme_images.WorkspaceThemeImages"
    ]
    """<p>The image assets used in the workspace theme.</p>"""
    typography: NotRequired[
        "capo_connect.types.workspace_theme_typography.WorkspaceThemeTypography"
    ]
    """<p>The typography configuration for the workspace theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceThemeConfig) -> dict:
    out: dict = {}
    if "palette" in value:
        import capo_connect.types.workspace_theme_palette

        out["Palette"] = capo_connect.types.workspace_theme_palette.serialize_json(
            value["palette"]
        )
    if "images" in value:
        import capo_connect.types.workspace_theme_images

        out["Images"] = capo_connect.types.workspace_theme_images.serialize_json(
            value["images"]
        )
    if "typography" in value:
        import capo_connect.types.workspace_theme_typography

        out["Typography"] = (
            capo_connect.types.workspace_theme_typography.serialize_json(
                value["typography"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkspaceThemeConfig:
    out: WorkspaceThemeConfig = {}  # type: ignore[typeddict-item]
    if "Palette" in data:
        import capo_connect.types.workspace_theme_palette

        out["palette"] = capo_connect.types.workspace_theme_palette.deserialize_json(
            data["Palette"]
        )
    if "Images" in data:
        import capo_connect.types.workspace_theme_images

        out["images"] = capo_connect.types.workspace_theme_images.deserialize_json(
            data["Images"]
        )
    if "Typography" in data:
        import capo_connect.types.workspace_theme_typography

        out["typography"] = (
            capo_connect.types.workspace_theme_typography.deserialize_json(
                data["Typography"]
            )
        )
    return out
