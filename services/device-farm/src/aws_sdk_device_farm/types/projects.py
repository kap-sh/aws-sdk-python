"""Generated from Smithy shape ``com.amazonaws.devicefarm#Projects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.project

Projects: TypeAlias = list["aws_sdk_device_farm.types.project.Project"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Projects) -> list:
    import aws_sdk_device_farm.types.project

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.project.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Projects:
    import aws_sdk_device_farm.types.project

    out: Projects = []
    for item in data:
        out.append(aws_sdk_device_farm.types.project.deserialize_aws_json_1_1(item))
    return out
