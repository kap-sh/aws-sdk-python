"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.summarization_dimension_detail

SummarizationDimensionDetails: TypeAlias = list[
    "capo_notifications.types.summarization_dimension_detail.SummarizationDimensionDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionDetails) -> list:
    import capo_notifications.types.summarization_dimension_detail

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.summarization_dimension_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SummarizationDimensionDetails:
    import capo_notifications.types.summarization_dimension_detail

    out: SummarizationDimensionDetails = []
    for item in data:
        out.append(
            capo_notifications.types.summarization_dimension_detail.deserialize_json(
                item
            )
        )
    return out
