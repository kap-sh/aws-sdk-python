"""Generated from Smithy shape ``com.amazonaws.emr#InstanceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceState: TypeAlias = Literal[
    "AWAITING_FULFILLMENT",
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "TERMINATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWAITING_FULFILLMENT",
        "PROVISIONING",
        "BOOTSTRAPPING",
        "RUNNING",
        "TERMINATED",
    )
)


def serialize_aws_json_1_1(value: InstanceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceState value: {data!r}")
    return cast(InstanceState, data)
