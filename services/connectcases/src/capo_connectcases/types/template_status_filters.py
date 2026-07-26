"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateStatusFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.template_status

TemplateStatusFilters: TypeAlias = list[
    "capo_connectcases.types.template_status.TemplateStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStatusFilters) -> list:
    return list(value)


def deserialize_json(data: list) -> TemplateStatusFilters:
    return list(data)
