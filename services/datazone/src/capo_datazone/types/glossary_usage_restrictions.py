"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryUsageRestrictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.glossary_usage_restriction

GlossaryUsageRestrictions: TypeAlias = list[
    "capo_datazone.types.glossary_usage_restriction.GlossaryUsageRestriction"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryUsageRestrictions) -> list:
    import capo_datazone.types.glossary_usage_restriction

    out: list = []
    for item in value:
        out.append(capo_datazone.types.glossary_usage_restriction.serialize_json(item))
    return out


def deserialize_json(data: list) -> GlossaryUsageRestrictions:
    import capo_datazone.types.glossary_usage_restriction

    out: GlossaryUsageRestrictions = []
    for item in data:
        out.append(
            capo_datazone.types.glossary_usage_restriction.deserialize_json(item)
        )
    return out
