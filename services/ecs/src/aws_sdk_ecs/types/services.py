"""Generated from Smithy shape ``com.amazonaws.ecs#Services``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service

Services: TypeAlias = list["aws_sdk_ecs.types.service.Service"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Services) -> list:
    import aws_sdk_ecs.types.service

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Services:
    import aws_sdk_ecs.types.service

    out: Services = []
    for item in data:
        out.append(aws_sdk_ecs.types.service.deserialize_aws_json_1_1(item))
    return out
