"""Generated from Smithy shape ``com.amazonaws.glue#BatchPutDataQualityStatisticAnnotationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.annotation_error_list


class BatchPutDataQualityStatisticAnnotationResponse(TypedDict, closed=True):
    failed_inclusion_annotations: NotRequired[
        "aws_sdk_glue.types.annotation_error_list.AnnotationErrorList"
    ]
    """<p>A list of <code>AnnotationError</code>'s.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchPutDataQualityStatisticAnnotationResponse,
) -> dict:
    out: dict = {}
    if "failed_inclusion_annotations" in value:
        import aws_sdk_glue.types.annotation_error_list

        out["FailedInclusionAnnotations"] = (
            aws_sdk_glue.types.annotation_error_list.serialize_aws_json_1_1(
                value["failed_inclusion_annotations"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchPutDataQualityStatisticAnnotationResponse:
    out: BatchPutDataQualityStatisticAnnotationResponse = {}  # type: ignore[typeddict-item]
    if "FailedInclusionAnnotations" in data:
        import aws_sdk_glue.types.annotation_error_list

        out["failed_inclusion_annotations"] = (
            aws_sdk_glue.types.annotation_error_list.deserialize_aws_json_1_1(
                data["FailedInclusionAnnotations"]
            )
        )
    return out
