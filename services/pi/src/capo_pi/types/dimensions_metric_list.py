"""Generated from Smithy shape ``com.amazonaws.pi#DimensionsMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.sanitized_string

DimensionsMetricList: TypeAlias = list["capo_pi.types.sanitized_string.SanitizedString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionsMetricList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DimensionsMetricList:
    return list(data)
