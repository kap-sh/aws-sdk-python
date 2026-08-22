"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.ab_test_arn
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.ab_test_status
    import capo_bedrock_agentcore.types.gateway_arn


class ABTestSummary(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test.</p>"""
    ab_test_arn: "capo_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the A/B test.</p>"""
    name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName"
    """<p>The name of the A/B test.</p>"""
    status: "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The current status of the A/B test.</p>"""
    execution_status: (
        "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    )
    """<p>The execution status of the A/B test.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
    ]
    """<p>The description of the A/B test.</p>"""
    gateway_arn: NotRequired["capo_bedrock_agentcore.types.gateway_arn.GatewayArn"]
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
    import capo_bedrock_agentcore.types.ab_test_status

    out["status"] = capo_bedrock_agentcore.types.ab_test_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.ab_test_execution_status

    out["executionStatus"] = (
        capo_bedrock_agentcore.types.ab_test_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ABTestSummary:
    out: ABTestSummary = {}  # type: ignore[typeddict-item]
    if data.get("abTestId") is not None:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("ABTestSummary.ab_test_id required")
    if data.get("abTestArn") is not None:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("ABTestSummary.ab_test_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ABTestSummary.name required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.ab_test_status

        out["status"] = capo_bedrock_agentcore.types.ab_test_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ABTestSummary.status required")
    if data.get("executionStatus") is not None:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError("ABTestSummary.execution_status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ABTestSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("ABTestSummary.updated_at required")
    return out
