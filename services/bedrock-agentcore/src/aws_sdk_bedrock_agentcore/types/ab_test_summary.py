"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_arn
    import aws_sdk_bedrock_agentcore.types.ab_test_description
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    import aws_sdk_bedrock_agentcore.types.ab_test_id
    import aws_sdk_bedrock_agentcore.types.ab_test_name
    import aws_sdk_bedrock_agentcore.types.ab_test_status
    import aws_sdk_bedrock_agentcore.types.gateway_arn
    import datetime

class ABTestSummary(TypedDict):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test.</p>"""
    ab_test_arn: "aws_sdk_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the A/B test.</p>"""
    name: "aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"
    """<p>The name of the A/B test.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The current status of the A/B test.</p>"""
    execution_status: "aws_sdk_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    """<p>The execution status of the A/B test.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"]
    """<p>The description of the A/B test.</p>"""
    gateway_arn: NotRequired["aws_sdk_bedrock_agentcore.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway used for traffic splitting.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was last updated.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ABTestSummary) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.ab_test_status
    out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.serialize_json(value["status"])
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    out["executionStatus"] = aws_sdk_bedrock_agentcore.types.ab_test_execution_status.serialize_json(value["execution_status"])
    if "description" in value:
        out["description"] = value["description"]
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp
    out["updatedAt"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> ABTestSummary:
    out: ABTestSummary = {}  # type: ignore[typeddict-item]
    if "abTestId" in data:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("ABTestSummary.ab_test_id required")
    if "abTestArn" in data:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("ABTestSummary.ab_test_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ABTestSummary.name required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_status
        out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("ABTestSummary.status required")
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
        out["execution_status"] = aws_sdk_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(data["executionStatus"])
    else:
        raise DeserializationError("ABTestSummary.execution_status required")
    if "description" in data:
        out["description"] = data["description"]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("ABTestSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp
        out["updated_at"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(data["updatedAt"])
    else:
        raise DeserializationError("ABTestSummary.updated_at required")
    return out