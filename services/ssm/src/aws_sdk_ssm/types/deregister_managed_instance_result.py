"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterManagedInstanceResult``."""

from typing_extensions import TypedDict


class DeregisterManagedInstanceResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterManagedInstanceResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterManagedInstanceResult:
    out: DeregisterManagedInstanceResult = {}  # type: ignore[typeddict-item]
    return out
