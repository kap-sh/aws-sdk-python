"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

AssociatedResourceType: TypeAlias = Literal[
    "CLOUDFRONT",
    "API_GATEWAY",
    "COGNITO_USER_POOL",
    "APP_RUNNER_SERVICE",
    "VERIFIED_ACCESS_INSTANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFRONT",
        "API_GATEWAY",
        "COGNITO_USER_POOL",
        "APP_RUNNER_SERVICE",
        "VERIFIED_ACCESS_INSTANCE",
    )
)


def serialize_aws_json_1_1(value: AssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociatedResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociatedResourceType value: {data!r}")
    return cast(AssociatedResourceType, data)
