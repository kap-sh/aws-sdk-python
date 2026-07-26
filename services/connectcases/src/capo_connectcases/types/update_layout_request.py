"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateLayoutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.layout_content
    import capo_connectcases.types.layout_id
    import capo_connectcases.types.layout_name


class UpdateLayoutRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    layout_id: "capo_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""
    name: NotRequired["capo_connectcases.types.layout_name.LayoutName"]
    """<p>The name of the layout. It must be unique per domain.</p>"""
    content: NotRequired["capo_connectcases.types.layout_content.LayoutContent"]
    """<p>Information about which fields will be present in the layout, the order of the fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLayoutRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "content" in value:
        import capo_connectcases.types.layout_content

        out["content"] = capo_connectcases.types.layout_content.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLayoutRequest:
    out: UpdateLayoutRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "content" in data:
        import capo_connectcases.types.layout_content

        out["content"] = capo_connectcases.types.layout_content.deserialize_json(
            data["content"]
        )
    return out
