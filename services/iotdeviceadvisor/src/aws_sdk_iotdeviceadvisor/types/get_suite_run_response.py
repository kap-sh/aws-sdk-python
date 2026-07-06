"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name
    import aws_sdk_iotdeviceadvisor.types.error_reason
    import aws_sdk_iotdeviceadvisor.types.suite_definition_version
    import aws_sdk_iotdeviceadvisor.types.suite_run_configuration
    import aws_sdk_iotdeviceadvisor.types.suite_run_status
    import aws_sdk_iotdeviceadvisor.types.tag_map
    import aws_sdk_iotdeviceadvisor.types.test_result
    import aws_sdk_iotdeviceadvisor.types.timestamp
    import aws_sdk_iotdeviceadvisor.types.uuid


class GetSuiteRunResponse(TypedDict, closed=True):
    suite_definition_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite definition ID for the test suite run.</p>"""
    suite_definition_version: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version for the test suite run.</p>"""
    suite_run_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite run ID for the test suite run.</p>"""
    suite_run_arn: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the suite run.</p>"""
    suite_run_configuration: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_run_configuration.SuiteRunConfiguration"
    ]
    """<p>Suite run configuration for the test suite run.</p>"""
    test_result: NotRequired["aws_sdk_iotdeviceadvisor.types.test_result.TestResult"]
    """<p>Test results for the test suite run.</p>"""
    start_time: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the test suite run started.</p>"""
    end_time: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the test suite run ended.</p>"""
    status: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_run_status.SuiteRunStatus"
    ]
    """<p>Status for the test suite run.</p>"""
    error_reason: NotRequired["aws_sdk_iotdeviceadvisor.types.error_reason.ErrorReason"]
    """<p>Error reason for any test suite run failure.</p>"""
    tags: NotRequired["aws_sdk_iotdeviceadvisor.types.tag_map.TagMap"]
    """<p>The tags attached to the suite run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteRunResponse) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_version" in value:
        out["suiteDefinitionVersion"] = value["suite_definition_version"]
    if "suite_run_id" in value:
        out["suiteRunId"] = value["suite_run_id"]
    if "suite_run_arn" in value:
        out["suiteRunArn"] = value["suite_run_arn"]
    if "suite_run_configuration" in value:
        import aws_sdk_iotdeviceadvisor.types.suite_run_configuration

        out["suiteRunConfiguration"] = (
            aws_sdk_iotdeviceadvisor.types.suite_run_configuration.serialize_json(
                value["suite_run_configuration"]
            )
        )
    if "test_result" in value:
        import aws_sdk_iotdeviceadvisor.types.test_result

        out["testResult"] = aws_sdk_iotdeviceadvisor.types.test_result.serialize_json(
            value["test_result"]
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
    if "status" in value:
        import aws_sdk_iotdeviceadvisor.types.suite_run_status

        out["status"] = aws_sdk_iotdeviceadvisor.types.suite_run_status.serialize_json(
            value["status"]
        )
    if "error_reason" in value:
        out["errorReason"] = value["error_reason"]
    if "tags" in value:
        import aws_sdk_iotdeviceadvisor.types.tag_map

        out["tags"] = aws_sdk_iotdeviceadvisor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetSuiteRunResponse:
    out: GetSuiteRunResponse = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionVersion" in data:
        out["suite_definition_version"] = data["suiteDefinitionVersion"]
    if "suiteRunId" in data:
        out["suite_run_id"] = data["suiteRunId"]
    if "suiteRunArn" in data:
        out["suite_run_arn"] = data["suiteRunArn"]
    if "suiteRunConfiguration" in data:
        import aws_sdk_iotdeviceadvisor.types.suite_run_configuration

        out["suite_run_configuration"] = (
            aws_sdk_iotdeviceadvisor.types.suite_run_configuration.deserialize_json(
                data["suiteRunConfiguration"]
            )
        )
    if "testResult" in data:
        import aws_sdk_iotdeviceadvisor.types.test_result

        out["test_result"] = (
            aws_sdk_iotdeviceadvisor.types.test_result.deserialize_json(
                data["testResult"]
            )
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
    if "status" in data:
        import aws_sdk_iotdeviceadvisor.types.suite_run_status

        out["status"] = (
            aws_sdk_iotdeviceadvisor.types.suite_run_status.deserialize_json(
                data["status"]
            )
        )
    if "errorReason" in data:
        out["error_reason"] = data["errorReason"]
    if "tags" in data:
        import aws_sdk_iotdeviceadvisor.types.tag_map

        out["tags"] = aws_sdk_iotdeviceadvisor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
