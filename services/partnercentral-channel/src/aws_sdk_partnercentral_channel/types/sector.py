"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Sector``."""

from typing import Literal, TypeAlias, cast

Sector: TypeAlias = Literal[
    "COMMERCIAL",
    "GOVERNMENT",
    "GOVERNMENT_EXCEPTION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Sector) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Sector:
    return cast(Sector, data)
