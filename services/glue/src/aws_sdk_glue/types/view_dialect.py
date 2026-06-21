"""Generated from Smithy shape ``com.amazonaws.glue#ViewDialect``."""

from typing import Literal, TypeAlias, cast

ViewDialect: TypeAlias = Literal[
    "REDSHIFT",
    "ATHENA",
    "SPARK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewDialect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViewDialect:
    return cast(ViewDialect, data)
