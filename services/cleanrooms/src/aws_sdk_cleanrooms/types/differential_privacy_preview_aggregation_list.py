"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyPreviewAggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation

DifferentialPrivacyPreviewAggregationList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation.DifferentialPrivacyPreviewAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyPreviewAggregationList) -> list:
    import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DifferentialPrivacyPreviewAggregationList:
    import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation

    out: DifferentialPrivacyPreviewAggregationList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation.deserialize_json(
                item
            )
        )
    return out
