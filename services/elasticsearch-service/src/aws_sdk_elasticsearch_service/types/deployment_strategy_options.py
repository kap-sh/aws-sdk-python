"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeploymentStrategyOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.deployment_strategy


class DeploymentStrategyOptions(TypedDict, closed=True):
    deployment_strategy: (
        "aws_sdk_elasticsearch_service.types.deployment_strategy.DeploymentStrategy"
    )
    """<p>Specifies the deployment strategy for the domain. Valid values are <code>Default</code> and <code>CapacityOptimized</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOptions) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.deployment_strategy

    out["DeploymentStrategy"] = (
        aws_sdk_elasticsearch_service.types.deployment_strategy.serialize_json(
            value["deployment_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeploymentStrategyOptions:
    out: DeploymentStrategyOptions = {}  # type: ignore[typeddict-item]
    if "DeploymentStrategy" in data:
        import aws_sdk_elasticsearch_service.types.deployment_strategy

        out["deployment_strategy"] = (
            aws_sdk_elasticsearch_service.types.deployment_strategy.deserialize_json(
                data["DeploymentStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "DeploymentStrategyOptions.deployment_strategy required"
        )
    return out
