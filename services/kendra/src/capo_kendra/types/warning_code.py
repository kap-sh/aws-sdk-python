"""Generated from Smithy shape ``com.amazonaws.kendra#WarningCode``."""

from typing import Literal, TypeAlias, cast

WarningCode: TypeAlias = Literal["QUERY_LANGUAGE_INVALID_SYNTAX",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarningCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WarningCode:
    return cast(WarningCode, data)
