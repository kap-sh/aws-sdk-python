"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelMatchScope``."""

from typing import Literal, TypeAlias, cast

LabelMatchScope: TypeAlias = Literal[
    "LABEL",
    "NAMESPACE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelMatchScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelMatchScope:
    return cast(LabelMatchScope, data)
