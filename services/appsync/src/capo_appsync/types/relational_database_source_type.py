"""Generated from Smithy shape ``com.amazonaws.appsync#RelationalDatabaseSourceType``."""

from typing import Literal, TypeAlias, cast

RelationalDatabaseSourceType: TypeAlias = Literal["RDS_HTTP_ENDPOINT",]


# --- restJson1 ser/de ---
def serialize_json(value: RelationalDatabaseSourceType) -> str:
    return value


def deserialize_json(data: str) -> RelationalDatabaseSourceType:
    return cast(RelationalDatabaseSourceType, data)
