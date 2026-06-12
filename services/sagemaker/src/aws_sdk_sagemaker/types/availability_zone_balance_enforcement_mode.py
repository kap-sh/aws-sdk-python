"""Generated from Smithy shape ``com.amazonaws.sagemaker#AvailabilityZoneBalanceEnforcementMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AvailabilityZoneBalanceEnforcementMode: TypeAlias = Literal["PERMISSIVE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PERMISSIVE",))


def serialize_aws_json_1_1(value: AvailabilityZoneBalanceEnforcementMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityZoneBalanceEnforcementMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AvailabilityZoneBalanceEnforcementMode value: {data!r}"
        )
    return cast(AvailabilityZoneBalanceEnforcementMode, data)
