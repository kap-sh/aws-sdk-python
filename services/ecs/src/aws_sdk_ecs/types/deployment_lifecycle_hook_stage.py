"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStage``."""

from typing import Literal, TypeAlias

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
