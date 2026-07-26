"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteRunInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.suite_definition_name
    import capo_iotdeviceadvisor.types.suite_definition_version
    import capo_iotdeviceadvisor.types.suite_run_result_count
    import capo_iotdeviceadvisor.types.suite_run_status
    import capo_iotdeviceadvisor.types.timestamp
    import capo_iotdeviceadvisor.types.uuid


class SuiteRunInformation(TypedDict, closed=True):
    suite_definition_id: NotRequired["capo_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite definition ID of the suite run.</p>"""
    suite_definition_version: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version of the suite run.</p>"""
    suite_definition_name: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_name.SuiteDefinitionName"
    ]
    """<p>Suite definition name of the suite run.</p>"""
    suite_run_id: NotRequired["capo_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite run ID of the suite run.</p>"""
    created_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the suite run was created.</p>"""
    started_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the suite run was started.</p>"""
    end_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the suite run ended.</p>"""
    status: NotRequired["capo_iotdeviceadvisor.types.suite_run_status.SuiteRunStatus"]
    """<p>Status of the suite run.</p>"""
    passed: NotRequired[
        "capo_iotdeviceadvisor.types.suite_run_result_count.SuiteRunResultCount"
    ]
    """<p>Number of test cases that passed in the suite run.</p>"""
    failed: NotRequired[
        "capo_iotdeviceadvisor.types.suite_run_result_count.SuiteRunResultCount"
    ]
    """<p>Number of test cases that failed in the suite run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuiteRunInformation) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_version" in value:
        out["suiteDefinitionVersion"] = value["suite_definition_version"]
    if "suite_definition_name" in value:
        out["suiteDefinitionName"] = value["suite_definition_name"]
    if "suite_run_id" in value:
        out["suiteRunId"] = value["suite_run_id"]
    if "created_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["createdAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "started_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["startedAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "end_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["endAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["end_at"]
        )
    if "status" in value:
        import capo_iotdeviceadvisor.types.suite_run_status

        out["status"] = capo_iotdeviceadvisor.types.suite_run_status.serialize_json(
            value["status"]
        )
    if "passed" in value:
        out["passed"] = value["passed"]
    if "failed" in value:
        out["failed"] = value["failed"]
    return out


def deserialize_json(data: dict) -> SuiteRunInformation:
    out: SuiteRunInformation = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionVersion" in data:
        out["suite_definition_version"] = data["suiteDefinitionVersion"]
    if "suiteDefinitionName" in data:
        out["suite_definition_name"] = data["suiteDefinitionName"]
    if "suiteRunId" in data:
        out["suite_run_id"] = data["suiteRunId"]
    if "createdAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["created_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "startedAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["started_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["end_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["endAt"]
        )
    if "status" in data:
        import capo_iotdeviceadvisor.types.suite_run_status

        out["status"] = capo_iotdeviceadvisor.types.suite_run_status.deserialize_json(
            data["status"]
        )
    if "passed" in data:
        out["passed"] = data["passed"]
    if "failed" in data:
        out["failed"] = data["failed"]
    return out
