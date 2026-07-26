"""Generated from Smithy shape ``com.amazonaws.glue#PutDataQualityProfileAnnotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.inclusion_annotation_value


class PutDataQualityProfileAnnotationRequest(TypedDict, closed=True):
    profile_id: "capo_glue.types.hash_string.HashString"
    """<p>The ID of the data quality monitoring profile to annotate.</p>"""
    inclusion_annotation: (
        "capo_glue.types.inclusion_annotation_value.InclusionAnnotationValue"
    )
    """<p>The inclusion annotation value to apply to the profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDataQualityProfileAnnotationRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_glue.types.inclusion_annotation_value

    out["InclusionAnnotation"] = (
        capo_glue.types.inclusion_annotation_value.serialize_aws_json_1_1(
            value["inclusion_annotation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDataQualityProfileAnnotationRequest:
    out: PutDataQualityProfileAnnotationRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError(
            "PutDataQualityProfileAnnotationRequest.profile_id required"
        )
    if "InclusionAnnotation" in data:
        import capo_glue.types.inclusion_annotation_value

        out["inclusion_annotation"] = (
            capo_glue.types.inclusion_annotation_value.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    else:
        raise DeserializationError(
            "PutDataQualityProfileAnnotationRequest.inclusion_annotation required"
        )
    return out
