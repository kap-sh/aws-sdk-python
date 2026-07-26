"""Generated from Smithy shape ``com.amazonaws.glue#BatchPutDataQualityStatisticAnnotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.inclusion_annotation_list


class BatchPutDataQualityStatisticAnnotationRequest(TypedDict, closed=True):
    inclusion_annotations: (
        "capo_glue.types.inclusion_annotation_list.InclusionAnnotationList"
    )
    """<p>A list of <code>DatapointInclusionAnnotation</code>'s. The InclusionAnnotations must contain a profileId and statisticId. If there are multiple InclusionAnnotations, the list must refer to a single statisticId across multiple profileIds.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>Client Token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchPutDataQualityStatisticAnnotationRequest,
) -> dict:
    out: dict = {}
    import capo_glue.types.inclusion_annotation_list

    out["InclusionAnnotations"] = (
        capo_glue.types.inclusion_annotation_list.serialize_aws_json_1_1(
            value["inclusion_annotations"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchPutDataQualityStatisticAnnotationRequest:
    out: BatchPutDataQualityStatisticAnnotationRequest = {}  # type: ignore[typeddict-item]
    if "InclusionAnnotations" in data:
        import capo_glue.types.inclusion_annotation_list

        out["inclusion_annotations"] = (
            capo_glue.types.inclusion_annotation_list.deserialize_aws_json_1_1(
                data["InclusionAnnotations"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutDataQualityStatisticAnnotationRequest.inclusion_annotations required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
