"""Generated from Smithy shape ``com.amazonaws.glue#AnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.statistic_annotation

AnnotationList: TypeAlias = list[
    "aws_sdk_glue.types.statistic_annotation.StatisticAnnotation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnnotationList) -> list:
    import aws_sdk_glue.types.statistic_annotation

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.statistic_annotation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AnnotationList:
    import aws_sdk_glue.types.statistic_annotation

    out: AnnotationList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.statistic_annotation.deserialize_aws_json_1_1(item)
        )
    return out
