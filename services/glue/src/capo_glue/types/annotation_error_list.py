"""Generated from Smithy shape ``com.amazonaws.glue#AnnotationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.annotation_error

AnnotationErrorList: TypeAlias = list[
    "capo_glue.types.annotation_error.AnnotationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnnotationErrorList) -> list:
    import capo_glue.types.annotation_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.annotation_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AnnotationErrorList:
    import capo_glue.types.annotation_error

    out: AnnotationErrorList = []
    for item in data:
        out.append(capo_glue.types.annotation_error.deserialize_aws_json_1_1(item))
    return out
