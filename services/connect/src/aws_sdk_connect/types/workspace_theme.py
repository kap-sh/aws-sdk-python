"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceTheme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.workspace_theme_config


class WorkspaceTheme(TypedDict, closed=True):
    light: NotRequired[
        "aws_sdk_connect.types.workspace_theme_config.WorkspaceThemeConfig"
    ]
    """<p>The theme configuration for light mode.</p>"""
    dark: NotRequired[
        "aws_sdk_connect.types.workspace_theme_config.WorkspaceThemeConfig"
    ]
    """<p>The theme configuration for dark mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceTheme) -> dict:
    out: dict = {}
    if "light" in value:
        import aws_sdk_connect.types.workspace_theme_config

        out["Light"] = aws_sdk_connect.types.workspace_theme_config.serialize_json(
            value["light"]
        )
    if "dark" in value:
        import aws_sdk_connect.types.workspace_theme_config

        out["Dark"] = aws_sdk_connect.types.workspace_theme_config.serialize_json(
            value["dark"]
        )
    return out


def deserialize_json(data: dict) -> WorkspaceTheme:
    out: WorkspaceTheme = {}  # type: ignore[typeddict-item]
    if "Light" in data:
        import aws_sdk_connect.types.workspace_theme_config

        out["light"] = aws_sdk_connect.types.workspace_theme_config.deserialize_json(
            data["Light"]
        )
    if "Dark" in data:
        import aws_sdk_connect.types.workspace_theme_config

        out["dark"] = aws_sdk_connect.types.workspace_theme_config.deserialize_json(
            data["Dark"]
        )
    return out
