"""Generated from Smithy shape ``com.amazonaws.glue#DatapointInclusionAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.inclusion_annotation_value


class DatapointInclusionAnnotation(TypedDict, closed=True):
    profile_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The ID of the data quality profile the statistic belongs to.</p>"""
    statistic_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    inclusion_annotation: NotRequired[
        "capo_glue.types.inclusion_annotation_value.InclusionAnnotationValue"
    ]
    """<p>The inclusion annotation value to apply to the statistic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatapointInclusionAnnotation) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "inclusion_annotation" in value:
        import capo_glue.types.inclusion_annotation_value

        out["InclusionAnnotation"] = (
            capo_glue.types.inclusion_annotation_value.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatapointInclusionAnnotation:
    out: DatapointInclusionAnnotation = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "InclusionAnnotation" in data:
        import capo_glue.types.inclusion_annotation_value

        out["inclusion_annotation"] = (
            capo_glue.types.inclusion_annotation_value.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out
