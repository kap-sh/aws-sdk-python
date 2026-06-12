"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capture_option

CaptureOptionList: TypeAlias = list[
    "aws_sdk_sagemaker.types.capture_option.CaptureOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptureOptionList) -> list:
    import aws_sdk_sagemaker.types.capture_option

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.capture_option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CaptureOptionList:
    import aws_sdk_sagemaker.types.capture_option

    out: CaptureOptionList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.capture_option.deserialize_aws_json_1_1(item)
        )
    return out
