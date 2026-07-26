"""Generated from Smithy shape ``com.amazonaws.forecast#Domain``."""

from typing import Literal, TypeAlias, cast

Domain: TypeAlias = Literal[
    "RETAIL",
    "CUSTOM",
    "INVENTORY_PLANNING",
    "EC2_CAPACITY",
    "WORK_FORCE",
    "WEB_TRAFFIC",
    "METRICS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Domain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Domain:
    return cast(Domain, data)
