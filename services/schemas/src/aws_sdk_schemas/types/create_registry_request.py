"""Generated from Smithy shape ``com.amazonaws.schemas#CreateRegistryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__string_min0_max256
    import aws_sdk_schemas.types.tags


class CreateRegistryRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>A description of the registry to be created.</p>"""
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags to associate with the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRegistryRequest:
    out: CreateRegistryRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    return out
