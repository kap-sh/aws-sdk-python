"""Generated from Smithy shape ``com.amazonaws.glue#AnnotationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.annotation_error

AnnotationErrorList: TypeAlias = list[
    "aws_sdk_glue.types.annotation_error.AnnotationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnnotationErrorList) -> list:
    import aws_sdk_glue.types.annotation_error

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.annotation_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AnnotationErrorList:
    import aws_sdk_glue.types.annotation_error

    out: AnnotationErrorList = []
    for item in data:
        out.append(aws_sdk_glue.types.annotation_error.deserialize_aws_json_1_1(item))
    return out
