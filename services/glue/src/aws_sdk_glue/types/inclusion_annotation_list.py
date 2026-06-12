"""Generated from Smithy shape ``com.amazonaws.glue#InclusionAnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.datapoint_inclusion_annotation

InclusionAnnotationList: TypeAlias = list[
    "aws_sdk_glue.types.datapoint_inclusion_annotation.DatapointInclusionAnnotation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionAnnotationList) -> list:
    import aws_sdk_glue.types.datapoint_inclusion_annotation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.datapoint_inclusion_annotation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InclusionAnnotationList:
    import aws_sdk_glue.types.datapoint_inclusion_annotation

    out: InclusionAnnotationList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.datapoint_inclusion_annotation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
