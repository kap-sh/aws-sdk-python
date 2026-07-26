"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.test_grid_session_action

TestGridSessionActions: TypeAlias = list[
    "capo_device_farm.types.test_grid_session_action.TestGridSessionAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionActions) -> list:
    import capo_device_farm.types.test_grid_session_action

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.test_grid_session_action.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestGridSessionActions:
    import capo_device_farm.types.test_grid_session_action

    out: TestGridSessionActions = []
    for item in data:
        out.append(
            capo_device_farm.types.test_grid_session_action.deserialize_aws_json_1_1(
                item
            )
        )
    return out
