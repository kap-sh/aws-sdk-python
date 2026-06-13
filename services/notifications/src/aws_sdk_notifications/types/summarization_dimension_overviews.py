"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionOverviews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.summarization_dimension_overview

SummarizationDimensionOverviews: TypeAlias = list[
    "aws_sdk_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionOverviews) -> list:
    import aws_sdk_notifications.types.summarization_dimension_overview

    out: list = []
    for item in value:
        out.append(
            aws_sdk_notifications.types.summarization_dimension_overview.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SummarizationDimensionOverviews:
    import aws_sdk_notifications.types.summarization_dimension_overview

    out: SummarizationDimensionOverviews = []
    for item in data:
        out.append(
            aws_sdk_notifications.types.summarization_dimension_overview.deserialize_json(
                item
            )
        )
    return out
