"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.failure
    import aws_sdk_iotdeviceadvisor.types.log_url
    import aws_sdk_iotdeviceadvisor.types.status
    import aws_sdk_iotdeviceadvisor.types.test_case_definition_name
    import aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list
    import aws_sdk_iotdeviceadvisor.types.timestamp
    import aws_sdk_iotdeviceadvisor.types.uuid
    import aws_sdk_iotdeviceadvisor.types.warnings


class TestCaseRun(TypedDict, closed=True):
    test_case_run_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Provides the test case run ID.</p>"""
    test_case_definition_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Provides the test case run definition ID.</p>"""
    test_case_definition_name: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.test_case_definition_name.TestCaseDefinitionName"
    ]
    """<p>Provides the test case run definition name.</p>"""
    status: NotRequired["aws_sdk_iotdeviceadvisor.types.status.Status"]
    """<p>Provides the test case run status. Status is one of the following:</p> <ul> <li> <p> <code>PASS</code>: Test passed.</p> </li> <li> <p> <code>FAIL</code>: Test failed.</p> </li> <li> <p> <code>PENDING</code>: Test has not started running but is scheduled.</p> </li> <li> <p> <code>RUNNING</code>: Test is running.</p> </li> <li> <p> <code>STOPPING</code>: Test is performing cleanup steps. You will see this status only if you stop a suite run.</p> </li> <li> <p> <code>STOPPED</code> Test is stopped. You will see this status only if you stop a suite run.</p> </li> <li> <p> <code>PASS_WITH_WARNINGS</code>: Test passed with warnings.</p> </li> <li> <p> <code>ERORR</code>: Test faced an error when running due to an internal issue.</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Provides test case run start time.</p>"""
    end_time: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Provides test case run end time.</p>"""
    log_url: NotRequired["aws_sdk_iotdeviceadvisor.types.log_url.LogUrl"]
    """<p>Provides test case run log URL.</p>"""
    warnings: NotRequired["aws_sdk_iotdeviceadvisor.types.warnings.Warnings"]
    """<p>Provides test case run warnings.</p>"""
    failure: NotRequired["aws_sdk_iotdeviceadvisor.types.failure.Failure"]
    """<p>Provides test case run failure result.</p>"""
    test_scenarios: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list.TestCaseScenariosList"
    ]
    """<p> Provides the test scenarios for the test case run. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseRun) -> dict:
    out: dict = {}
    if "test_case_run_id" in value:
        out["testCaseRunId"] = value["test_case_run_id"]
    if "test_case_definition_id" in value:
        out["testCaseDefinitionId"] = value["test_case_definition_id"]
    if "test_case_definition_name" in value:
        out["testCaseDefinitionName"] = value["test_case_definition_name"]
    if "status" in value:
        import aws_sdk_iotdeviceadvisor.types.status

        out["status"] = aws_sdk_iotdeviceadvisor.types.status.serialize_json(
            value["status"]
        )
    if "start_time" in value:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["startTime"] = aws_sdk_iotdeviceadvisor.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["endTime"] = aws_sdk_iotdeviceadvisor.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "log_url" in value:
        out["logUrl"] = value["log_url"]
    if "warnings" in value:
        out["warnings"] = value["warnings"]
    if "failure" in value:
        out["failure"] = value["failure"]
    if "test_scenarios" in value:
        import aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list

        out["testScenarios"] = (
            aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list.serialize_json(
                value["test_scenarios"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestCaseRun:
    out: TestCaseRun = {}  # type: ignore[typeddict-item]
    if "testCaseRunId" in data:
        out["test_case_run_id"] = data["testCaseRunId"]
    if "testCaseDefinitionId" in data:
        out["test_case_definition_id"] = data["testCaseDefinitionId"]
    if "testCaseDefinitionName" in data:
        out["test_case_definition_name"] = data["testCaseDefinitionName"]
    if "status" in data:
        import aws_sdk_iotdeviceadvisor.types.status

        out["status"] = aws_sdk_iotdeviceadvisor.types.status.deserialize_json(
            data["status"]
        )
    if "startTime" in data:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["start_time"] = aws_sdk_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["end_time"] = aws_sdk_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "logUrl" in data:
        out["log_url"] = data["logUrl"]
    if "warnings" in data:
        out["warnings"] = data["warnings"]
    if "failure" in data:
        out["failure"] = data["failure"]
    if "testScenarios" in data:
        import aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list

        out["test_scenarios"] = (
            aws_sdk_iotdeviceadvisor.types.test_case_scenarios_list.deserialize_json(
                data["testScenarios"]
            )
        )
    return out
