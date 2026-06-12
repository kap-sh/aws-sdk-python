"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#XAxisValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.long

XAxisValues: TypeAlias = list["aws_sdk_sagemaker_metrics.types.long.Long"]


# --- restJson1 ser/de ---
def serialize_json(value: XAxisValues) -> list:
    return list(value)


def deserialize_json(data: list) -> XAxisValues:
    return list(data)
