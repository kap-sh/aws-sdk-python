"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateStatus``."""

from typing import Literal, TypeAlias, cast

TemplateStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> TemplateStatus:
    return cast(TemplateStatus, data)
