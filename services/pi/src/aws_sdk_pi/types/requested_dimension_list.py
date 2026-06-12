"""Generated from Smithy shape ``com.amazonaws.pi#RequestedDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.sanitized_string

RequestedDimensionList: TypeAlias = list[
    "aws_sdk_pi.types.sanitized_string.SanitizedString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestedDimensionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RequestedDimensionList:
    return list(data)
