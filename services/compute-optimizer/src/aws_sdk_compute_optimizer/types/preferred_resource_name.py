"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResourceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

PreferredResourceName: TypeAlias = Literal["Ec2InstanceTypes",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Ec2InstanceTypes",))


def serialize_aws_json_1_0(value: PreferredResourceName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreferredResourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreferredResourceName value: {data!r}")
    return cast(PreferredResourceName, data)
