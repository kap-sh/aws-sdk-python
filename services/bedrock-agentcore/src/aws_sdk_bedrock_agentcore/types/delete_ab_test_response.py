"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteABTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_arn
    import aws_sdk_bedrock_agentcore.types.ab_test_id
    import aws_sdk_bedrock_agentcore.types.ab_test_status


class DeleteABTestResponse(TypedDict, closed=True):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the deleted A/B test.</p>"""
    ab_test_arn: "aws_sdk_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the deleted A/B test.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The status of the A/B test deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    import aws_sdk_bedrock_agentcore.types.ab_test_status

    out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteABTestResponse:
    out: DeleteABTestResponse = {}  # type: ignore[typeddict-item]
    if "abTestId" in data:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("DeleteABTestResponse.ab_test_id required")
    if "abTestArn" in data:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("DeleteABTestResponse.ab_test_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_status

        out["status"] = aws_sdk_bedrock_agentcore.types.ab_test_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteABTestResponse.status required")
    return out
