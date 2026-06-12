"""Generated from Smithy shape ``com.amazonaws.ssm#TargetLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.target_location

TargetLocations: TypeAlias = list["aws_sdk_ssm.types.target_location.TargetLocation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetLocations) -> list:
    import aws_sdk_ssm.types.target_location

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.target_location.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetLocations:
    import aws_sdk_ssm.types.target_location

    out: TargetLocations = []
    for item in data:
        out.append(aws_sdk_ssm.types.target_location.deserialize_aws_json_1_1(item))
    return out
