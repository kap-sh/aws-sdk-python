"""Generated from Smithy shape ``com.amazonaws.iot#TemplateType``."""

from typing import Literal, TypeAlias, cast

TemplateType: TypeAlias = Literal[
    "FLEET_PROVISIONING",
    "JITP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateType) -> str:
    return value


def deserialize_json(data: str) -> TemplateType:
    return cast(TemplateType, data)
