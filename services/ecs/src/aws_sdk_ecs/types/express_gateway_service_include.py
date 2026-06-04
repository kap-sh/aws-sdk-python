"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceInclude``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ExpressGatewayServiceInclude: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: ExpressGatewayServiceInclude) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceInclude:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExpressGatewayServiceInclude value: {data!r}"
        )
    return cast(ExpressGatewayServiceInclude, data)
