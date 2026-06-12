"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.tag_key
    import aws_sdk_lex_model_building_service.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_lex_model_building_service.types.tag_key.TagKey"
    """<p>The key for the tag. Keys are not case-sensitive and must be unique.</p>"""
    value: "aws_sdk_lex_model_building_service.types.tag_value.TagValue"
    """<p>The value associated with a key. The value may be an empty string but it can't be null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
