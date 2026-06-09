"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentLifecycleStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: ServiceDeploymentLifecycleStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceDeploymentLifecycleStage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceDeploymentLifecycleStage value: {data!r}"
        )
    return cast(ServiceDeploymentLifecycleStage, data)
