"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentLifecycleStage``."""

from typing import Literal, TypeAlias

ServiceDeploymentLifecycleStage: TypeAlias = Literal[
    "RECONCILE_SERVICE",
    "PRE_SCALE_UP",
    "SCALE_UP",
    "POST_SCALE_UP",
    "TEST_TRAFFIC_SHIFT",
    "POST_TEST_TRAFFIC_SHIFT",
    "PRODUCTION_TRAFFIC_SHIFT",
    "POST_PRODUCTION_TRAFFIC_SHIFT",
    "BAKE_TIME",
    "CLEAN_UP",
]
