"""Generated from Smithy shape ``com.amazonaws.sagemaker#AvailabilityZoneBalanceEnforcementMode``."""

from typing import Literal, TypeAlias, cast

AvailabilityZoneBalanceEnforcementMode: TypeAlias = Literal["PERMISSIVE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZoneBalanceEnforcementMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityZoneBalanceEnforcementMode:
    return cast(AvailabilityZoneBalanceEnforcementMode, data)
