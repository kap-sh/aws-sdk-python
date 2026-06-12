"""Generated from Smithy shape ``com.amazonaws.lightsail#EstimatesByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.estimate_by_time

EstimatesByTime: TypeAlias = list[
    "aws_sdk_lightsail.types.estimate_by_time.EstimateByTime"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EstimatesByTime) -> list:
    import aws_sdk_lightsail.types.estimate_by_time

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.estimate_by_time.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EstimatesByTime:
    import aws_sdk_lightsail.types.estimate_by_time

    out: EstimatesByTime = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.estimate_by_time.deserialize_aws_json_1_1(item)
        )
    return out
