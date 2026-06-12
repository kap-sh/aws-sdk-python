"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.deployment_impairment_strategy
    import aws_sdk_gamelift.types.deployment_protection_strategy
    import aws_sdk_gamelift.types.minimum_healthy_percentage


class DeploymentConfiguration(TypedDict):
    protection_strategy: NotRequired[
        "aws_sdk_gamelift.types.deployment_protection_strategy.DeploymentProtectionStrategy"
    ]
    """<p>Determines how fleet deployment activity affects active game sessions on the fleet. With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection. </p>"""
    minimum_healthy_percentage: NotRequired[
        "aws_sdk_gamelift.types.minimum_healthy_percentage.MinimumHealthyPercentage"
    ]
    """<p>Sets a minimum level of healthy tasks to maintain during deployment activity. </p>"""
    impairment_strategy: NotRequired[
        "aws_sdk_gamelift.types.deployment_impairment_strategy.DeploymentImpairmentStrategy"
    ]
    """<p>Determines what actions to take if a deployment fails. If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfiguration) -> dict:
    out: dict = {}
    if "protection_strategy" in value:
        import aws_sdk_gamelift.types.deployment_protection_strategy

        out["ProtectionStrategy"] = (
            aws_sdk_gamelift.types.deployment_protection_strategy.serialize_aws_json_1_1(
                value["protection_strategy"]
            )
        )
    if "minimum_healthy_percentage" in value:
        out["MinimumHealthyPercentage"] = value["minimum_healthy_percentage"]
    if "impairment_strategy" in value:
        import aws_sdk_gamelift.types.deployment_impairment_strategy

        out["ImpairmentStrategy"] = (
            aws_sdk_gamelift.types.deployment_impairment_strategy.serialize_aws_json_1_1(
                value["impairment_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfiguration:
    out: DeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if "ProtectionStrategy" in data:
        import aws_sdk_gamelift.types.deployment_protection_strategy

        out["protection_strategy"] = (
            aws_sdk_gamelift.types.deployment_protection_strategy.deserialize_aws_json_1_1(
                data["ProtectionStrategy"]
            )
        )
    if "MinimumHealthyPercentage" in data:
        out["minimum_healthy_percentage"] = data["MinimumHealthyPercentage"]
    if "ImpairmentStrategy" in data:
        import aws_sdk_gamelift.types.deployment_impairment_strategy

        out["impairment_strategy"] = (
            aws_sdk_gamelift.types.deployment_impairment_strategy.deserialize_aws_json_1_1(
                data["ImpairmentStrategy"]
            )
        )
    return out
