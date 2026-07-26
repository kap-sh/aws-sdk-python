"""Generated from Smithy shape ``com.amazonaws.inspector#ScopeType``."""

from typing import Literal, TypeAlias, cast

ScopeType: TypeAlias = Literal[
    "INSTANCE_ID",
    "RULES_PACKAGE_ARN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScopeType:
    return cast(ScopeType, data)
