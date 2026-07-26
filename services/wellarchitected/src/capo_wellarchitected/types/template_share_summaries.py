"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TemplateShareSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.template_share_summary

TemplateShareSummaries: TypeAlias = list[
    "capo_wellarchitected.types.template_share_summary.TemplateShareSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateShareSummaries) -> list:
    import capo_wellarchitected.types.template_share_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.template_share_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateShareSummaries:
    import capo_wellarchitected.types.template_share_summary

    out: TemplateShareSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.template_share_summary.deserialize_json(item)
        )
    return out
