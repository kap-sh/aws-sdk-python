"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedQueryType``."""

from typing import Literal, TypeAlias, cast

GeneratedQueryType: TypeAlias = Literal["REDSHIFT_SQL",]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedQueryType) -> str:
    return value


def deserialize_json(data: str) -> GeneratedQueryType:
    return cast(GeneratedQueryType, data)
