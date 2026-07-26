"""Generated from Smithy shape ``com.amazonaws.glue#TimestampedInclusionAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.inclusion_annotation_value
    import capo_glue.types.timestamp


class TimestampedInclusionAnnotation(TypedDict, closed=True):
    value: NotRequired[
        "capo_glue.types.inclusion_annotation_value.InclusionAnnotationValue"
    ]
    """<p>The inclusion annotation value.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the inclusion annotation was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampedInclusionAnnotation) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_glue.types.inclusion_annotation_value

        out["Value"] = (
            capo_glue.types.inclusion_annotation_value.serialize_aws_json_1_1(
                value["value"]
            )
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp

        out["LastModifiedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampedInclusionAnnotation:
    out: TimestampedInclusionAnnotation = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import capo_glue.types.inclusion_annotation_value

        out["value"] = (
            capo_glue.types.inclusion_annotation_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    if "LastModifiedOn" in data:
        import capo_glue.types.timestamp

        out["last_modified_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    return out
