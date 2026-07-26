"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionOverviews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.summarization_dimension_overview

SummarizationDimensionOverviews: TypeAlias = list[
    "capo_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionOverviews) -> list:
    import capo_notifications.types.summarization_dimension_overview

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.summarization_dimension_overview.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SummarizationDimensionOverviews:
    import capo_notifications.types.summarization_dimension_overview

    out: SummarizationDimensionOverviews = []
    for item in data:
        out.append(
            capo_notifications.types.summarization_dimension_overview.deserialize_json(
                item
            )
        )
    return out
