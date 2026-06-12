"""Generated from Smithy shape ``com.amazonaws.fms#ResourceViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_violation

ResourceViolations: TypeAlias = list[
    "aws_sdk_fms.types.resource_violation.ResourceViolation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceViolations) -> list:
    import aws_sdk_fms.types.resource_violation

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.resource_violation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceViolations:
    import aws_sdk_fms.types.resource_violation

    out: ResourceViolations = []
    for item in data:
        out.append(aws_sdk_fms.types.resource_violation.deserialize_aws_json_1_1(item))
    return out
