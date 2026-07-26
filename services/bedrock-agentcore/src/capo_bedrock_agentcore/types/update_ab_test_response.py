"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateABTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.ab_test_arn
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_status


class UpdateABTestResponse(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the updated A/B test.</p>"""
    ab_test_arn: "capo_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the updated A/B test.</p>"""
    status: "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The status of the A/B test.</p>"""
    execution_status: (
        "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    )
    """<p>The execution status of the A/B test.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
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
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateABTestResponse:
    out: UpdateABTestResponse = {}  # type: ignore[typeddict-item]
    if "abTestId" in data:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("UpdateABTestResponse.ab_test_id required")
    if "abTestArn" in data:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("UpdateABTestResponse.ab_test_arn required")
    if "status" in data:
        import capo_bedrock_agentcore.types.ab_test_status

        out["status"] = capo_bedrock_agentcore.types.ab_test_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateABTestResponse.status required")
    if "executionStatus" in data:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateABTestResponse.execution_status required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateABTestResponse.updated_at required")
    return out
