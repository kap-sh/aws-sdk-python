"""Generated from Smithy shape ``com.amazonaws.glue#SourceControlProvider``."""

from typing import Literal, TypeAlias, cast

SourceControlProvider: TypeAlias = Literal[
    "GITHUB",
    "GITLAB",
    "BITBUCKET",
    "AWS_CODE_COMMIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceControlProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceControlProvider:
    return cast(SourceControlProvider, data)
