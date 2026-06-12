"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionHeaderSuccessValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.success_value

ResponseInspectionHeaderSuccessValues: TypeAlias = list[
    "aws_sdk_wafv2.types.success_value.SuccessValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionHeaderSuccessValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResponseInspectionHeaderSuccessValues:
    return list(data)
