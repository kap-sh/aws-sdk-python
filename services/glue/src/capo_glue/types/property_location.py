"""Generated from Smithy shape ``com.amazonaws.glue#PropertyLocation``."""

from typing import Literal, TypeAlias, cast

PropertyLocation: TypeAlias = Literal[
    "HEADER",
    "BODY",
    "QUERY_PARAM",
    "PATH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyLocation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyLocation:
    return cast(PropertyLocation, data)
