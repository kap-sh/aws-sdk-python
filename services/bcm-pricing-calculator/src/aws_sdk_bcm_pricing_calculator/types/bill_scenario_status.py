"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioStatus``."""

from typing import Literal, TypeAlias, cast

BillScenarioStatus: TypeAlias = Literal[
    "READY",
    "LOCKED",
    "FAILED",
    "STALE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillScenarioStatus:
    return cast(BillScenarioStatus, data)
