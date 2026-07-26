"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FindingReasonCode``."""

from typing import Literal, TypeAlias, cast

FindingReasonCode: TypeAlias = Literal[
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FindingReasonCode:
    return cast(FindingReasonCode, data)
