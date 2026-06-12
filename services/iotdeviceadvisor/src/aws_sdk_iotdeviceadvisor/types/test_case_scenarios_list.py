"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenariosList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.test_case_scenario

TestCaseScenariosList: TypeAlias = list[
    "aws_sdk_iotdeviceadvisor.types.test_case_scenario.TestCaseScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseScenariosList) -> list:
    import aws_sdk_iotdeviceadvisor.types.test_case_scenario

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotdeviceadvisor.types.test_case_scenario.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestCaseScenariosList:
    import aws_sdk_iotdeviceadvisor.types.test_case_scenario

    out: TestCaseScenariosList = []
    for item in data:
        out.append(
            aws_sdk_iotdeviceadvisor.types.test_case_scenario.deserialize_json(item)
        )
    return out
