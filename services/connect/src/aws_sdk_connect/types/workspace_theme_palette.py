"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceThemePalette``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.palette_canvas
    import aws_sdk_connect.types.palette_header
    import aws_sdk_connect.types.palette_navigation
    import aws_sdk_connect.types.palette_primary


class WorkspaceThemePalette(TypedDict):
    header: NotRequired["aws_sdk_connect.types.palette_header.PaletteHeader"]
    """<p>The color configuration for the header area.</p>"""
    navigation: NotRequired[
        "aws_sdk_connect.types.palette_navigation.PaletteNavigation"
    ]
    """<p>The color configuration for the navigation area.</p>"""
    canvas: NotRequired["aws_sdk_connect.types.palette_canvas.PaletteCanvas"]
    """<p>The color configuration for the canvas area.</p>"""
    primary: NotRequired["aws_sdk_connect.types.palette_primary.PalettePrimary"]
    """<p>The primary color configuration used throughout the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceThemePalette) -> dict:
    out: dict = {}
    if "header" in value:
        import aws_sdk_connect.types.palette_header

        out["Header"] = aws_sdk_connect.types.palette_header.serialize_json(
            value["header"]
        )
    if "navigation" in value:
        import aws_sdk_connect.types.palette_navigation

        out["Navigation"] = aws_sdk_connect.types.palette_navigation.serialize_json(
            value["navigation"]
        )
    if "canvas" in value:
        import aws_sdk_connect.types.palette_canvas

        out["Canvas"] = aws_sdk_connect.types.palette_canvas.serialize_json(
            value["canvas"]
        )
    if "primary" in value:
        import aws_sdk_connect.types.palette_primary

        out["Primary"] = aws_sdk_connect.types.palette_primary.serialize_json(
            value["primary"]
        )
    return out


def deserialize_json(data: dict) -> WorkspaceThemePalette:
    out: WorkspaceThemePalette = {}  # type: ignore[typeddict-item]
    if "Header" in data:
        import aws_sdk_connect.types.palette_header

        out["header"] = aws_sdk_connect.types.palette_header.deserialize_json(
            data["Header"]
        )
    if "Navigation" in data:
        import aws_sdk_connect.types.palette_navigation

        out["navigation"] = aws_sdk_connect.types.palette_navigation.deserialize_json(
            data["Navigation"]
        )
    if "Canvas" in data:
        import aws_sdk_connect.types.palette_canvas

        out["canvas"] = aws_sdk_connect.types.palette_canvas.deserialize_json(
            data["Canvas"]
        )
    if "Primary" in data:
        import aws_sdk_connect.types.palette_primary

        out["primary"] = aws_sdk_connect.types.palette_primary.deserialize_json(
            data["Primary"]
        )
    return out
