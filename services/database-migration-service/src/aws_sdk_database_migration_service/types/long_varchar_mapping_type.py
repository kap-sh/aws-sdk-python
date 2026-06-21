"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#LongVarcharMappingType``."""

from typing import Literal, TypeAlias, cast

LongVarcharMappingType: TypeAlias = Literal[
    "wstring",
    "clob",
    "nclob",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongVarcharMappingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LongVarcharMappingType:
    return cast(LongVarcharMappingType, data)
