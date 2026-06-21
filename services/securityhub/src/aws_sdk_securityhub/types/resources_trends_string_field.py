"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringField``."""

from typing import Literal, TypeAlias, cast

ResourcesTrendsStringField: TypeAlias = Literal[
    "account_id",
    "region",
    "resource_type",
    "resource_category",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsStringField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesTrendsStringField:
    return cast(ResourcesTrendsStringField, data)
