"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaTemplateBodyExampleParams``."""

from typing import TypeAlias

MetaTemplateBodyExampleParams: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: MetaTemplateBodyExampleParams) -> list:
    return list(value)


def deserialize_json(data: list) -> MetaTemplateBodyExampleParams:
    return list(data)
