"""Generated from Smithy shape ``com.amazonaws.schemas#UpdateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.__string_min0_max36
    import capo_schemas.types.__string_min0_max256
    import capo_schemas.types.__string_min1_max100000
    import capo_schemas.types.type


class UpdateSchemaRequest(TypedDict, closed=True):
    client_token_id: NotRequired[
        "capo_schemas.types.__string_min0_max36.__stringMin0Max36"
    ]
    """<p>The ID of the client token.</p>"""
    content: NotRequired[
        "capo_schemas.types.__string_min1_max100000.__stringMin1Max100000"
    ]
    """<p>The source of the schema definition.</p>"""
    description: NotRequired[
        "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>The description of the schema.</p>"""
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "capo_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    type: NotRequired["capo_schemas.types.type.Type"]
    """<p>The schema type for the events schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaRequest) -> dict:
    out: dict = {}
    if "client_token_id" in value:
        out["ClientTokenId"] = value["client_token_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_schemas.types.type

        out["Type"] = capo_schemas.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UpdateSchemaRequest:
    out: UpdateSchemaRequest = {}  # type: ignore[typeddict-item]
    if "ClientTokenId" in data:
        out["client_token_id"] = data["ClientTokenId"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import capo_schemas.types.type

        out["type"] = capo_schemas.types.type.deserialize_json(data["Type"])
    return out
