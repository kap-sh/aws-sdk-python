"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal["CODESTAR",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    return cast(SourceType, data)
