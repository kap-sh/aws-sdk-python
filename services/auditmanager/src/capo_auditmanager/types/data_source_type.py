"""Generated from Smithy shape ``com.amazonaws.auditmanager#DataSourceType``."""

from typing import Literal, TypeAlias, cast

DataSourceType: TypeAlias = Literal[
    "AWS_Cloudtrail",
    "AWS_Config",
    "AWS_Security_Hub",
    "AWS_API_Call",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    return cast(DataSourceType, data)
