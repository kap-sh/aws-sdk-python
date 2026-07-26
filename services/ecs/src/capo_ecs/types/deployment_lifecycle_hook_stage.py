"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStage``."""

from typing import Literal, TypeAlias, cast

DeploymentLifecycleHookStage: TypeAlias = Literal[
    "RECONCILE_SERVICE",
    "PRE_SCALE_UP",
    "POST_SCALE_UP",
    "TEST_TRAFFIC_SHIFT",
    "POST_TEST_TRAFFIC_SHIFT",
    "PRE_PRODUCTION_TRAFFIC_SHIFT",
    "PRODUCTION_TRAFFIC_SHIFT",
    "POST_PRODUCTION_TRAFFIC_SHIFT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookStage:
    return cast(DeploymentLifecycleHookStage, data)
