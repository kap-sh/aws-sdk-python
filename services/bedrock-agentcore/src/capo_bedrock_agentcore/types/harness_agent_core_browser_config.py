"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessAgentCoreBrowserConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_browser_arn


class HarnessAgentCoreBrowserConfig(TypedDict, closed=True):
    browser_arn: NotRequired[
        "capo_bedrock_agentcore.types.harness_browser_arn.HarnessBrowserArn"
    ]
    """<p>If not populated, the built-in Browser ARN is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreBrowserConfig) -> dict:
    out: dict = {}
    if "browser_arn" in value:
        out["browserArn"] = value["browser_arn"]
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreBrowserConfig:
    out: HarnessAgentCoreBrowserConfig = {}  # type: ignore[typeddict-item]
    if data.get("browserArn") is not None:
        out["browser_arn"] = data["browserArn"]
    return out
