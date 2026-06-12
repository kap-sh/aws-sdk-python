"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EBSFilterName: TypeAlias = Literal["Finding",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Finding",))


def serialize_aws_json_1_0(value: EBSFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EBSFilterName value: {data!r}")
    return cast(EBSFilterName, data)
