"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandElementStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.navbar_style


class BrandElementStyle(TypedDict, closed=True):
    navbar_style: NotRequired["capo_quicksight.types.navbar_style.NavbarStyle"]
    """<p>The navigation bar style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandElementStyle) -> dict:
    out: dict = {}
    if "navbar_style" in value:
        import capo_quicksight.types.navbar_style

        out["NavbarStyle"] = capo_quicksight.types.navbar_style.serialize_json(
            value["navbar_style"]
        )
    return out


def deserialize_json(data: dict) -> BrandElementStyle:
    out: BrandElementStyle = {}  # type: ignore[typeddict-item]
    if "NavbarStyle" in data:
        import capo_quicksight.types.navbar_style

        out["navbar_style"] = capo_quicksight.types.navbar_style.deserialize_json(
            data["NavbarStyle"]
        )
    return out
