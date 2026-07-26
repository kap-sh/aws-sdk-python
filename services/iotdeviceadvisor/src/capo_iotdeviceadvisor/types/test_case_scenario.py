"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.failure
    import capo_iotdeviceadvisor.types.system_message
    import capo_iotdeviceadvisor.types.test_case_scenario_id
    import capo_iotdeviceadvisor.types.test_case_scenario_status
    import capo_iotdeviceadvisor.types.test_case_scenario_type


class TestCaseScenario(TypedDict, closed=True):
    test_case_scenario_id: NotRequired[
        "capo_iotdeviceadvisor.types.test_case_scenario_id.TestCaseScenarioId"
    ]
    """<p>Provides test case scenario ID.</p>"""
    test_case_scenario_type: NotRequired[
        "capo_iotdeviceadvisor.types.test_case_scenario_type.TestCaseScenarioType"
    ]
    """<p>Provides test case scenario type. Type is one of the following:</p> <ul> <li> <p>Advanced</p> </li> <li> <p>Basic</p> </li> </ul>"""
    status: NotRequired[
        "capo_iotdeviceadvisor.types.test_case_scenario_status.TestCaseScenarioStatus"
    ]
    """<p>Provides the test case scenario status. Status is one of the following:</p> <ul> <li> <p> <code>PASS</code>: Test passed.</p> </li> <li> <p> <code>FAIL</code>: Test failed.</p> </li> <li> <p> <code>PENDING</code>: Test has not started running but is scheduled.</p> </li> <li> <p> <code>RUNNING</code>: Test is running.</p> </li> <li> <p> <code>STOPPING</code>: Test is performing cleanup steps. You will see this status only if you stop a suite run.</p> </li> <li> <p> <code>STOPPED</code> Test is stopped. You will see this status only if you stop a suite run.</p> </li> <li> <p> <code>PASS_WITH_WARNINGS</code>: Test passed with warnings.</p> </li> <li> <p> <code>ERORR</code>: Test faced an error when running due to an internal issue.</p> </li> </ul>"""
    failure: NotRequired["capo_iotdeviceadvisor.types.failure.Failure"]
    """<p>Provides test case scenario failure result.</p>"""
    system_message: NotRequired[
        "capo_iotdeviceadvisor.types.system_message.SystemMessage"
    ]
    """<p>Provides test case scenario system messages if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseScenario) -> dict:
    out: dict = {}
    if "test_case_scenario_id" in value:
        out["testCaseScenarioId"] = value["test_case_scenario_id"]
    if "test_case_scenario_type" in value:
        import capo_iotdeviceadvisor.types.test_case_scenario_type

        out["testCaseScenarioType"] = (
            capo_iotdeviceadvisor.types.test_case_scenario_type.serialize_json(
                value["test_case_scenario_type"]
            )
        )
    if "status" in value:
        import capo_iotdeviceadvisor.types.test_case_scenario_status

        out["status"] = (
            capo_iotdeviceadvisor.types.test_case_scenario_status.serialize_json(
                value["status"]
            )
        )
    if "failure" in value:
        out["failure"] = value["failure"]
    if "system_message" in value:
        out["systemMessage"] = value["system_message"]
    return out


def deserialize_json(data: dict) -> TestCaseScenario:
    out: TestCaseScenario = {}  # type: ignore[typeddict-item]
    if "testCaseScenarioId" in data:
        out["test_case_scenario_id"] = data["testCaseScenarioId"]
    if "testCaseScenarioType" in data:
        import capo_iotdeviceadvisor.types.test_case_scenario_type

        out["test_case_scenario_type"] = (
            capo_iotdeviceadvisor.types.test_case_scenario_type.deserialize_json(
                data["testCaseScenarioType"]
            )
        )
    if "status" in data:
        import capo_iotdeviceadvisor.types.test_case_scenario_status

        out["status"] = (
            capo_iotdeviceadvisor.types.test_case_scenario_status.deserialize_json(
                data["status"]
            )
        )
    if "failure" in data:
        out["failure"] = data["failure"]
    if "systemMessage" in data:
        out["system_message"] = data["systemMessage"]
    return out
