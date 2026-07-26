"""Generated from Smithy shape ``com.amazonaws.apprunner#SourceCodeVersionType``."""

from typing import Literal, TypeAlias, cast

SourceCodeVersionType: TypeAlias = Literal["BRANCH",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceCodeVersionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SourceCodeVersionType:
    return cast(SourceCodeVersionType, data)
