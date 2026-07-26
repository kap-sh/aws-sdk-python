"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthReason``."""

from typing import Literal, TypeAlias, cast

InstanceHealthReason: TypeAlias = Literal[
    "Lb.RegistrationInProgress",
    "Lb.InitialHealthChecking",
    "Lb.InternalError",
    "Instance.ResponseCodeMismatch",
    "Instance.Timeout",
    "Instance.FailedHealthChecks",
    "Instance.NotRegistered",
    "Instance.NotInUse",
    "Instance.DeregistrationInProgress",
    "Instance.InvalidState",
    "Instance.IpUnusable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthReason:
    return cast(InstanceHealthReason, data)
