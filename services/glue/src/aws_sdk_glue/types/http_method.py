"""Generated from Smithy shape ``com.amazonaws.glue#HTTPMethod``."""

from typing import Literal, TypeAlias, cast

HTTPMethod: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HTTPMethod:
    return cast(HTTPMethod, data)
