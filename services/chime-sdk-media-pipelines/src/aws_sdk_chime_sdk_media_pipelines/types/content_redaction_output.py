"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentRedactionOutput``."""

from typing import Literal, TypeAlias, cast

ContentRedactionOutput: TypeAlias = Literal[
    "redacted",
    "redacted_and_unredacted",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentRedactionOutput) -> str:
    return value


def deserialize_json(data: str) -> ContentRedactionOutput:
    return cast(ContentRedactionOutput, data)
