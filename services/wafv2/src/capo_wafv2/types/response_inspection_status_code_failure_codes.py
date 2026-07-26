"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionStatusCodeFailureCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.failure_code

ResponseInspectionStatusCodeFailureCodes: TypeAlias = list[
    "capo_wafv2.types.failure_code.FailureCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionStatusCodeFailureCodes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResponseInspectionStatusCodeFailureCodes:
    return list(data)
