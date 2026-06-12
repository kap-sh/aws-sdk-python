"""Generated from Smithy shape ``com.amazonaws.schemas#UpdateSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__string_min0_max36
    import aws_sdk_schemas.types.__string_min0_max256
    import aws_sdk_schemas.types.__string_min1_max100000
    import aws_sdk_schemas.types.type


class UpdateSchemaRequest(TypedDict):
    client_token_id: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max36.__stringMin0Max36"
    ]
    """<p>The ID of the client token.</p>"""
    content: NotRequired[
        "aws_sdk_schemas.types.__string_min1_max100000.__stringMin1Max100000"
    ]
    """<p>The source of the schema definition.</p>"""
    description: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>The description of the schema.</p>"""
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    type: NotRequired["aws_sdk_schemas.types.type.Type"]
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
        import aws_sdk_schemas.types.type

        out["Type"] = aws_sdk_schemas.types.type.serialize_json(value["type"])
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
        import aws_sdk_schemas.types.type

        out["type"] = aws_sdk_schemas.types.type.deserialize_json(data["Type"])
    return out
