"""Generated from Smithy shape ``com.amazonaws.wafv2#OversizeHandling``."""

from typing import Literal, TypeAlias, cast

OversizeHandling: TypeAlias = Literal[
    "CONTINUE",
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OversizeHandling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OversizeHandling:
    return cast(OversizeHandling, data)
