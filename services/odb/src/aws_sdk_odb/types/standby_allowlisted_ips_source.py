"""Generated from Smithy shape ``com.amazonaws.odb#StandbyAllowlistedIpsSource``."""

from typing import Literal, TypeAlias, cast

StandbyAllowlistedIpsSource: TypeAlias = Literal[
    "PRIMARY",
    "SEPARATE",
    "NOT_APPLICABLE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StandbyAllowlistedIpsSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StandbyAllowlistedIpsSource:
    return cast(StandbyAllowlistedIpsSource, data)
