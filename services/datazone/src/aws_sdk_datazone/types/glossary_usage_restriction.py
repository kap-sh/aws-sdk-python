"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryUsageRestriction``."""

from typing import Literal, TypeAlias, cast

GlossaryUsageRestriction: TypeAlias = Literal["ASSET_GOVERNED_TERMS",]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryUsageRestriction) -> str:
    return value


def deserialize_json(data: str) -> GlossaryUsageRestriction:
    return cast(GlossaryUsageRestriction, data)
