"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ExpressGatewayServiceStatusCode: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: ExpressGatewayServiceStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExpressGatewayServiceStatusCode value: {data!r}"
        )
    return cast(ExpressGatewayServiceStatusCode, data)
