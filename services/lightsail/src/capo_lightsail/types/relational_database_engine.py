"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseEngine``."""

from typing import Literal, TypeAlias, cast

RelationalDatabaseEngine: TypeAlias = Literal["mysql",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseEngine) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabaseEngine:
    return cast(RelationalDatabaseEngine, data)
