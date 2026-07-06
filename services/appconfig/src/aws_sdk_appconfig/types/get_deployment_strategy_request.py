"""Generated from Smithy shape ``com.amazonaws.appconfig#GetDeploymentStrategyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deployment_strategy_id


class GetDeploymentStrategyRequest(TypedDict, closed=True):
    deployment_strategy_id: (
        "aws_sdk_appconfig.types.deployment_strategy_id.DeploymentStrategyId"
    )
    """<p>The ID of the deployment strategy to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentStrategyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentStrategyRequest:
    out: GetDeploymentStrategyRequest = {}  # type: ignore[typeddict-item]
    return out
