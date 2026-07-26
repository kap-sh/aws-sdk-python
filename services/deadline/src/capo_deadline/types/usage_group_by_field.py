"""Generated from Smithy shape ``com.amazonaws.deadline#UsageGroupByField``."""

from typing import Literal, TypeAlias, cast

UsageGroupByField: TypeAlias = Literal[
    "QUEUE_ID",
    "FLEET_ID",
    "JOB_ID",
    "USER_ID",
    "USAGE_TYPE",
    "INSTANCE_TYPE",
    "LICENSE_PRODUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageGroupByField) -> str:
    return value


def deserialize_json(data: str) -> UsageGroupByField:
    return cast(UsageGroupByField, data)
