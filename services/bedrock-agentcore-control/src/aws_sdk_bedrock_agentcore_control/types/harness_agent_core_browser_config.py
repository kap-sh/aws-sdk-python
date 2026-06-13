"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreBrowserConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_browser_arn

class HarnessAgentCoreBrowserConfig(TypedDict):
    browser_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.harness_browser_arn.HarnessBrowserArn"]
    """<p>If not populated, the built-in Browser ARN is used.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreBrowserConfig) -> dict:
    out: dict = {}
    if "browser_arn" in value:
        out["browserArn"] = value["browser_arn"]
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreBrowserConfig:
    out: HarnessAgentCoreBrowserConfig = {}  # type: ignore[typeddict-item]
    if "browserArn" in data:
        out["browser_arn"] = data["browserArn"]
    return out