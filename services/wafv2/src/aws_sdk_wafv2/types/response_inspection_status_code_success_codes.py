"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionStatusCodeSuccessCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.success_code

ResponseInspectionStatusCodeSuccessCodes: TypeAlias = list[
    "aws_sdk_wafv2.types.success_code.SuccessCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionStatusCodeSuccessCodes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResponseInspectionStatusCodeSuccessCodes:
    return list(data)
