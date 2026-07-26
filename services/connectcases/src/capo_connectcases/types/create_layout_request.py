"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateLayoutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.layout_content
    import capo_connectcases.types.layout_name


class CreateLayoutRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    name: "capo_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout. It must be unique for the Cases domain.</p>"""
    content: "capo_connectcases.types.layout_content.LayoutContent"
    """<p>Information about which fields will be present in the layout, and information about the order of the fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLayoutRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_connectcases.types.layout_content

    out["content"] = capo_connectcases.types.layout_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> CreateLayoutRequest:
    out: CreateLayoutRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateLayoutRequest.name required")
    if "content" in data:
        import capo_connectcases.types.layout_content

        out["content"] = capo_connectcases.types.layout_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CreateLayoutRequest.content required")
    return out
