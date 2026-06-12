"""Generated from Smithy shape ``com.amazonaws.wafv2#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "APPLICATION_LOAD_BALANCER",
    "API_GATEWAY",
    "APPSYNC",
    "COGNITO_USER_POOL",
    "APP_RUNNER_SERVICE",
    "VERIFIED_ACCESS_INSTANCE",
    "AMPLIFY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION_LOAD_BALANCER",
        "API_GATEWAY",
        "APPSYNC",
        "COGNITO_USER_POOL",
        "APP_RUNNER_SERVICE",
        "VERIFIED_ACCESS_INSTANCE",
        "AMPLIFY",
    )
)


def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
