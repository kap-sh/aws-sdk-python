"""Generated from Smithy shape ``com.amazonaws.guardduty#CriterionKey``."""

from typing import Literal, TypeAlias, cast

CriterionKey: TypeAlias = Literal[
    "EC2_INSTANCE_ARN",
    "SCAN_ID",
    "ACCOUNT_ID",
    "GUARDDUTY_FINDING_ID",
    "SCAN_START_TIME",
    "SCAN_STATUS",
    "SCAN_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CriterionKey) -> str:
    return value


def deserialize_json(data: str) -> CriterionKey:
    return cast(CriterionKey, data)
