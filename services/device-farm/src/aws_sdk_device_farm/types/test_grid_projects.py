"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridProjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.test_grid_project

TestGridProjects: TypeAlias = list[
    "aws_sdk_device_farm.types.test_grid_project.TestGridProject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridProjects) -> list:
    import aws_sdk_device_farm.types.test_grid_project

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.test_grid_project.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestGridProjects:
    import aws_sdk_device_farm.types.test_grid_project

    out: TestGridProjects = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.test_grid_project.deserialize_aws_json_1_1(item)
        )
    return out
