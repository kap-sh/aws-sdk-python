"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenariosList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.test_case_scenario

TestCaseScenariosList: TypeAlias = list[
    "capo_iotdeviceadvisor.types.test_case_scenario.TestCaseScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseScenariosList) -> list:
    import capo_iotdeviceadvisor.types.test_case_scenario

    out: list = []
    for item in value:
        out.append(capo_iotdeviceadvisor.types.test_case_scenario.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseScenariosList:
    import capo_iotdeviceadvisor.types.test_case_scenario

    out: TestCaseScenariosList = []
    for item in data:
        out.append(
            capo_iotdeviceadvisor.types.test_case_scenario.deserialize_json(item)
        )
    return out
