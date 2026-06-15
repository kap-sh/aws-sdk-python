"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteABTestRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_id


class DeleteABTestRequest(TypedDict):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteABTestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteABTestRequest:
    out: DeleteABTestRequest = {}  # type: ignore[typeddict-item]
    return out
