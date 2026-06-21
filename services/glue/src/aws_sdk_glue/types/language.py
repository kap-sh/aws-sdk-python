"""Generated from Smithy shape ``com.amazonaws.glue#Language``."""

from typing import Literal, TypeAlias, cast

Language: TypeAlias = Literal[
    "PYTHON",
    "SCALA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Language) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Language:
    return cast(Language, data)
