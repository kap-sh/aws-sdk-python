"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnrollmentFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EnrollmentFilterName: TypeAlias = Literal["Status",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Status",))


def serialize_aws_json_1_0(value: EnrollmentFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnrollmentFilterName value: {data!r}")
    return cast(EnrollmentFilterName, data)
