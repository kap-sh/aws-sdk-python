"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateABTestResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_arn
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    import aws_sdk_bedrock_agentcore.types.ab_test_id
    import aws_sdk_bedrock_agentcore.types.ab_test_name
    import aws_sdk_bedrock_agentcore.types.ab_test_status
    import datetime

class CreateABTestResponse(TypedDict):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the created A/B test.</p>"""
    ab_test_arn: "aws_sdk_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the created A/B test.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"]
    """<p>The name of the A/B test.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The status of the A/B test.</p>"""
    execution_status: "aws_sdk_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    """<p>The execution status indicating whether the A/B test is currently running.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.ab_test_status
    out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.serialize_json(value["status"])
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    out["executionStatus"] = aws_sdk_bedrock_agentcore.types.ab_test_execution_status.serialize_json(value["execution_status"])
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateABTestResponse:
    out: CreateABTestResponse = {}  # type: ignore[typeddict-item]
    if "abTestId" in data:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("CreateABTestResponse.ab_test_id required")
    if "abTestArn" in data:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("CreateABTestResponse.ab_test_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_status
        out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateABTestResponse.status required")
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
        out["execution_status"] = aws_sdk_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(data["executionStatus"])
    else:
        raise DeserializationError("CreateABTestResponse.execution_status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateABTestResponse.created_at required")
    return out