"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteDeploymentStrategyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_strategy_id


class DeleteDeploymentStrategyRequest(TypedDict, closed=True):
    deployment_strategy_id: (
        "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId"
    )
    """<p>The ID of the deployment strategy you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentStrategyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeploymentStrategyRequest:
    out: DeleteDeploymentStrategyRequest = {}  # type: ignore[typeddict-item]
    return out
