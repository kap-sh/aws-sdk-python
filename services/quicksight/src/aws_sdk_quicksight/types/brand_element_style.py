"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandElementStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.navbar_style


class BrandElementStyle(TypedDict):
    navbar_style: NotRequired["aws_sdk_quicksight.types.navbar_style.NavbarStyle"]
    """<p>The navigation bar style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandElementStyle) -> dict:
    out: dict = {}
    if "navbar_style" in value:
        import aws_sdk_quicksight.types.navbar_style

        out["NavbarStyle"] = aws_sdk_quicksight.types.navbar_style.serialize_json(
            value["navbar_style"]
        )
    return out


def deserialize_json(data: dict) -> BrandElementStyle:
    out: BrandElementStyle = {}  # type: ignore[typeddict-item]
    if "NavbarStyle" in data:
        import aws_sdk_quicksight.types.navbar_style

        out["navbar_style"] = aws_sdk_quicksight.types.navbar_style.deserialize_json(
            data["NavbarStyle"]
        )
    return out
