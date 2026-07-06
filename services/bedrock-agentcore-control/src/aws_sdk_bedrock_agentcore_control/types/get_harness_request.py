"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetHarnessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_id


class GetHarnessRequest(TypedDict, closed=True):
    harness_id: "aws_sdk_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarnessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHarnessRequest:
    out: GetHarnessRequest = {}  # type: ignore[typeddict-item]
    return out
