"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#StartSuiteRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name
    import aws_sdk_iotdeviceadvisor.types.endpoint
    import aws_sdk_iotdeviceadvisor.types.timestamp
    import aws_sdk_iotdeviceadvisor.types.uuid


class StartSuiteRunResponse(TypedDict, closed=True):
    suite_run_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite Run ID of the started suite run.</p>"""
    suite_run_arn: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Amazon Resource Name (ARN) of the started suite run.</p>"""
    created_at: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Starts a Device Advisor test suite run based on suite create time.</p>"""
    endpoint: NotRequired["aws_sdk_iotdeviceadvisor.types.endpoint.Endpoint"]
    """<p>The response of an Device Advisor test endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSuiteRunResponse) -> dict:
    out: dict = {}
    if "suite_run_id" in value:
        out["suiteRunId"] = value["suite_run_id"]
    if "suite_run_arn" in value:
        out["suiteRunArn"] = value["suite_run_arn"]
    if "created_at" in value:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["createdAt"] = aws_sdk_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> StartSuiteRunResponse:
    out: StartSuiteRunResponse = {}  # type: ignore[typeddict-item]
    if "suiteRunId" in data:
        out["suite_run_id"] = data["suiteRunId"]
    if "suiteRunArn" in data:
        out["suite_run_arn"] = data["suiteRunArn"]
    if "createdAt" in data:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["created_at"] = aws_sdk_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    return out
