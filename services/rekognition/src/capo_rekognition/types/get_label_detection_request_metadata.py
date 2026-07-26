"""Generated from Smithy shape ``com.amazonaws.rekognition#GetLabelDetectionRequestMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.label_detection_aggregate_by
    import capo_rekognition.types.label_detection_sort_by


class GetLabelDetectionRequestMetadata(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_rekognition.types.label_detection_sort_by.LabelDetectionSortBy"
    ]
    """<p>The sorting method chosen for a GetLabelDetection request.</p>"""
    aggregate_by: NotRequired[
        "capo_rekognition.types.label_detection_aggregate_by.LabelDetectionAggregateBy"
    ]
    """<p>The aggregation method chosen for a GetLabelDetection request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLabelDetectionRequestMetadata) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_rekognition.types.label_detection_sort_by

        out["SortBy"] = (
            capo_rekognition.types.label_detection_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "aggregate_by" in value:
        import capo_rekognition.types.label_detection_aggregate_by

        out["AggregateBy"] = (
            capo_rekognition.types.label_detection_aggregate_by.serialize_aws_json_1_1(
                value["aggregate_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLabelDetectionRequestMetadata:
    out: GetLabelDetectionRequestMetadata = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import capo_rekognition.types.label_detection_sort_by

        out["sort_by"] = (
            capo_rekognition.types.label_detection_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "AggregateBy" in data:
        import capo_rekognition.types.label_detection_aggregate_by

        out["aggregate_by"] = (
            capo_rekognition.types.label_detection_aggregate_by.deserialize_aws_json_1_1(
                data["AggregateBy"]
            )
        )
    return out
