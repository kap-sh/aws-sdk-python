"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityStatisticAnnotationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.annotation_list
    import aws_sdk_glue.types.pagination_token


class ListDataQualityStatisticAnnotationsResponse(TypedDict):
    annotations: NotRequired["aws_sdk_glue.types.annotation_list.AnnotationList"]
    """<p>A list of <code>StatisticAnnotation</code> applied to the Statistic</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityStatisticAnnotationsResponse) -> dict:
    out: dict = {}
    if "annotations" in value:
        import aws_sdk_glue.types.annotation_list

        out["Annotations"] = aws_sdk_glue.types.annotation_list.serialize_aws_json_1_1(
            value["annotations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityStatisticAnnotationsResponse:
    out: ListDataQualityStatisticAnnotationsResponse = {}  # type: ignore[typeddict-item]
    if "Annotations" in data:
        import aws_sdk_glue.types.annotation_list

        out["annotations"] = (
            aws_sdk_glue.types.annotation_list.deserialize_aws_json_1_1(
                data["Annotations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
