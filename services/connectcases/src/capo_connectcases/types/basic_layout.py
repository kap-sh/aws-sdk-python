"""Generated from Smithy shape ``com.amazonaws.connectcases#BasicLayout``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.layout_sections


class BasicLayout(TypedDict, closed=True):
    top_panel: NotRequired["capo_connectcases.types.layout_sections.LayoutSections"]
    """<p>This represents sections in a panel of the page layout.</p>"""
    more_info: NotRequired["capo_connectcases.types.layout_sections.LayoutSections"]
    """<p>This represents sections in a tab of the page layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicLayout) -> dict:
    out: dict = {}
    if "top_panel" in value:
        import capo_connectcases.types.layout_sections

        out["topPanel"] = capo_connectcases.types.layout_sections.serialize_json(
            value["top_panel"]
        )
    if "more_info" in value:
        import capo_connectcases.types.layout_sections

        out["moreInfo"] = capo_connectcases.types.layout_sections.serialize_json(
            value["more_info"]
        )
    return out


def deserialize_json(data: dict) -> BasicLayout:
    out: BasicLayout = {}  # type: ignore[typeddict-item]
    if "topPanel" in data:
        import capo_connectcases.types.layout_sections

        out["top_panel"] = capo_connectcases.types.layout_sections.deserialize_json(
            data["topPanel"]
        )
    if "moreInfo" in data:
        import capo_connectcases.types.layout_sections

        out["more_info"] = capo_connectcases.types.layout_sections.deserialize_json(
            data["moreInfo"]
        )
    return out
