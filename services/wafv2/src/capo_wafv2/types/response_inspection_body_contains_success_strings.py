"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionBodyContainsSuccessStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.success_value

ResponseInspectionBodyContainsSuccessStrings: TypeAlias = list[
    "capo_wafv2.types.success_value.SuccessValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionBodyContainsSuccessStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(
    data: list,
) -> ResponseInspectionBodyContainsSuccessStrings:
    return list(data)
