"""Generated from Smithy shape ``com.amazonaws.quicksight#NavbarStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.palette


class NavbarStyle(TypedDict, closed=True):
    global_navbar: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The global navigation bar style.</p>"""
    contextual_navbar: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The contextual navigation bar style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NavbarStyle) -> dict:
    out: dict = {}
    if "global_navbar" in value:
        import aws_sdk_quicksight.types.palette

        out["GlobalNavbar"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["global_navbar"]
        )
    if "contextual_navbar" in value:
        import aws_sdk_quicksight.types.palette

        out["ContextualNavbar"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["contextual_navbar"]
        )
    return out


def deserialize_json(data: dict) -> NavbarStyle:
    out: NavbarStyle = {}  # type: ignore[typeddict-item]
    if "GlobalNavbar" in data:
        import aws_sdk_quicksight.types.palette

        out["global_navbar"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["GlobalNavbar"]
        )
    if "ContextualNavbar" in data:
        import aws_sdk_quicksight.types.palette

        out["contextual_navbar"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["ContextualNavbar"]
        )
    return out
