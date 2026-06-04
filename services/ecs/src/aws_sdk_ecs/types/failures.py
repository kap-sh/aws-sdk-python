"""Generated from Smithy shape ``com.amazonaws.ecs#Failures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failure

Failures: TypeAlias = list["aws_sdk_ecs.types.failure.Failure"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Failures) -> list:
    import aws_sdk_ecs.types.failure

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Failures:
    import aws_sdk_ecs.types.failure

    out: Failures = []
    for item in data:
        out.append(aws_sdk_ecs.types.failure.deserialize_aws_json_1_1(item))
    return out
