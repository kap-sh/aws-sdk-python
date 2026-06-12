"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseName: TypeAlias = Literal["SQLServer",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SQLServer",))


def serialize_aws_json_1_0(value: LicenseName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseName value: {data!r}")
    return cast(LicenseName, data)
