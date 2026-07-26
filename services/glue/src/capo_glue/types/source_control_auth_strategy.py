"""Generated from Smithy shape ``com.amazonaws.glue#SourceControlAuthStrategy``."""

from typing import Literal, TypeAlias, cast

SourceControlAuthStrategy: TypeAlias = Literal[
    "PERSONAL_ACCESS_TOKEN",
    "AWS_SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceControlAuthStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceControlAuthStrategy:
    return cast(SourceControlAuthStrategy, data)
