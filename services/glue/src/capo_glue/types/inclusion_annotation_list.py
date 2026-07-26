"""Generated from Smithy shape ``com.amazonaws.glue#InclusionAnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.datapoint_inclusion_annotation

InclusionAnnotationList: TypeAlias = list[
    "capo_glue.types.datapoint_inclusion_annotation.DatapointInclusionAnnotation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionAnnotationList) -> list:
    import capo_glue.types.datapoint_inclusion_annotation

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.datapoint_inclusion_annotation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InclusionAnnotationList:
    import capo_glue.types.datapoint_inclusion_annotation

    out: InclusionAnnotationList = []
    for item in data:
        out.append(
            capo_glue.types.datapoint_inclusion_annotation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
