"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingAggregationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_scan_finding_aggregation

ImageScanFindingAggregationsList: TypeAlias = list[
    "capo_imagebuilder.types.image_scan_finding_aggregation.ImageScanFindingAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingAggregationsList) -> list:
    import capo_imagebuilder.types.image_scan_finding_aggregation

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.image_scan_finding_aggregation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImageScanFindingAggregationsList:
    import capo_imagebuilder.types.image_scan_finding_aggregation

    out: ImageScanFindingAggregationsList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.image_scan_finding_aggregation.deserialize_json(
                item
            )
        )
    return out
