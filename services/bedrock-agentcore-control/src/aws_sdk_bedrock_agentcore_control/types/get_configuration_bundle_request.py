"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetConfigurationBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.branch_name
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id


class GetConfigurationBundleRequest(TypedDict):
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle to retrieve.</p>"""
    branch_name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>The branch name to get the latest version from. If not specified, returns the latest version on the mainline branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationBundleRequest:
    out: GetConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    return out
