"""Generated from Smithy shape ``com.amazonaws.pi#AdditionalMetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.sanitized_string

AdditionalMetricsList: TypeAlias = list[
    "aws_sdk_pi.types.sanitized_string.SanitizedString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalMetricsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AdditionalMetricsList:
    return list(data)
