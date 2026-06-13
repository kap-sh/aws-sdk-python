"""Generated from Smithy shape ``com.amazonaws.wisdom#Highlights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.highlight

Highlights: TypeAlias = list["aws_sdk_wisdom.types.highlight.Highlight"]


# --- restJson1 ser/de ---
def serialize_json(value: Highlights) -> list:
    import aws_sdk_wisdom.types.highlight

    out: list = []
    for item in value:
        out.append(aws_sdk_wisdom.types.highlight.serialize_json(item))
    return out


def deserialize_json(data: list) -> Highlights:
    import aws_sdk_wisdom.types.highlight

    out: Highlights = []
    for item in data:
        out.append(aws_sdk_wisdom.types.highlight.deserialize_json(item))
    return out
