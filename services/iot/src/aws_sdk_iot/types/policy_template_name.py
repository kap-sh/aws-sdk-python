"""Generated from Smithy shape ``com.amazonaws.iot#PolicyTemplateName``."""

from typing import Literal, TypeAlias, cast

PolicyTemplateName: TypeAlias = Literal["BLANK_POLICY",]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyTemplateName) -> str:
    return value


def deserialize_json(data: str) -> PolicyTemplateName:
    return cast(PolicyTemplateName, data)
