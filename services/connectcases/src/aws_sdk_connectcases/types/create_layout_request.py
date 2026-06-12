"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateLayoutRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.layout_content
    import aws_sdk_connectcases.types.layout_name


class CreateLayoutRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    name: "aws_sdk_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout. It must be unique for the Cases domain.</p>"""
    content: "aws_sdk_connectcases.types.layout_content.LayoutContent"
    """<p>Information about which fields will be present in the layout, and information about the order of the fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLayoutRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_connectcases.types.layout_content

    out["content"] = aws_sdk_connectcases.types.layout_content.serialize_json(
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
        import aws_sdk_connectcases.types.layout_content

        out["content"] = aws_sdk_connectcases.types.layout_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CreateLayoutRequest.content required")
    return out
