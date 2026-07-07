"""Generated from Smithy shape ``com.amazonaws.rekognition#GetContentModerationRequestMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.content_moderation_aggregate_by
    import aws_sdk_rekognition.types.content_moderation_sort_by


class GetContentModerationRequestMetadata(TypedDict, closed=True):
    sort_by: NotRequired[
        "aws_sdk_rekognition.types.content_moderation_sort_by.ContentModerationSortBy"
    ]
    """<p>The sorting method chosen for a GetContentModeration request.</p>"""
    aggregate_by: NotRequired[
        "aws_sdk_rekognition.types.content_moderation_aggregate_by.ContentModerationAggregateBy"
    ]
    """<p>The aggregation method chosen for a GetContentModeration request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContentModerationRequestMetadata) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_rekognition.types.content_moderation_sort_by

        out["SortBy"] = (
            aws_sdk_rekognition.types.content_moderation_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "aggregate_by" in value:
        import aws_sdk_rekognition.types.content_moderation_aggregate_by

        out["AggregateBy"] = (
            aws_sdk_rekognition.types.content_moderation_aggregate_by.serialize_aws_json_1_1(
                value["aggregate_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContentModerationRequestMetadata:
    out: GetContentModerationRequestMetadata = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_rekognition.types.content_moderation_sort_by

        out["sort_by"] = (
            aws_sdk_rekognition.types.content_moderation_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "AggregateBy" in data:
        import aws_sdk_rekognition.types.content_moderation_aggregate_by

        out["aggregate_by"] = (
            aws_sdk_rekognition.types.content_moderation_aggregate_by.deserialize_aws_json_1_1(
                data["AggregateBy"]
            )
        )
    return out
