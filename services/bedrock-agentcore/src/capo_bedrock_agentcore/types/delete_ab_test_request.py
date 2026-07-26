"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteABTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_id


class DeleteABTestRequest(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteABTestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteABTestRequest:
    out: DeleteABTestRequest = {}  # type: ignore[typeddict-item]
    return out
