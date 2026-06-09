"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ProxyConfigurationType: TypeAlias = Literal["APPMESH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPMESH",))


def serialize_aws_json_1_1(value: ProxyConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProxyConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProxyConfigurationType value: {data!r}")
    return cast(ProxyConfigurationType, data)
