"""Generated from Smithy shape ``com.amazonaws.kendra#HighlightType``."""

from typing import Literal, TypeAlias, cast

HighlightType: TypeAlias = Literal[
    "STANDARD",
    "THESAURUS_SYNONYM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HighlightType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HighlightType:
    return cast(HighlightType, data)
