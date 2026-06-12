"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionHeaderFailureValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.failure_value

ResponseInspectionHeaderFailureValues: TypeAlias = list[
    "aws_sdk_wafv2.types.failure_value.FailureValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionHeaderFailureValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResponseInspectionHeaderFailureValues:
    return list(data)
