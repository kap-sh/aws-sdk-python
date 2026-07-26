"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfClassificationScopeSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.classification_scope_summary

__listOfClassificationScopeSummary: TypeAlias = list[
    "capo_macie2.types.classification_scope_summary.ClassificationScopeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClassificationScopeSummary) -> list:
    import capo_macie2.types.classification_scope_summary

    out: list = []
    for item in value:
        out.append(capo_macie2.types.classification_scope_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClassificationScopeSummary:
    import capo_macie2.types.classification_scope_summary

    out: __listOfClassificationScopeSummary = []
    for item in data:
        out.append(
            capo_macie2.types.classification_scope_summary.deserialize_json(item)
        )
    return out
