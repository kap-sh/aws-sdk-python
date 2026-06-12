"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.test_grid_session

TestGridSessions: TypeAlias = list[
    "aws_sdk_device_farm.types.test_grid_session.TestGridSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessions) -> list:
    import aws_sdk_device_farm.types.test_grid_session

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.test_grid_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestGridSessions:
    import aws_sdk_device_farm.types.test_grid_session

    out: TestGridSessions = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.test_grid_session.deserialize_aws_json_1_1(item)
        )
    return out
