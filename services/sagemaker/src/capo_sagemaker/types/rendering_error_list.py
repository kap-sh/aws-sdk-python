"""Generated from Smithy shape ``com.amazonaws.sagemaker#RenderingErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.rendering_error

RenderingErrorList: TypeAlias = list[
    "capo_sagemaker.types.rendering_error.RenderingError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenderingErrorList) -> list:
    import capo_sagemaker.types.rendering_error

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.rendering_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RenderingErrorList:
    import capo_sagemaker.types.rendering_error

    out: RenderingErrorList = []
    for item in data:
        out.append(capo_sagemaker.types.rendering_error.deserialize_aws_json_1_1(item))
    return out
