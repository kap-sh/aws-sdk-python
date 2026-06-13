"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetABTestRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_id

class GetABTestRequest(TypedDict):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetABTestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetABTestRequest:
    out: GetABTestRequest = {}  # type: ignore[typeddict-item]
    return out