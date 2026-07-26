"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.review_template_summary

ReviewTemplates: TypeAlias = list[
    "capo_wellarchitected.types.review_template_summary.ReviewTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplates) -> list:
    import capo_wellarchitected.types.review_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.review_template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReviewTemplates:
    import capo_wellarchitected.types.review_template_summary

    out: ReviewTemplates = []
    for item in data:
        out.append(
            capo_wellarchitected.types.review_template_summary.deserialize_json(item)
        )
    return out
