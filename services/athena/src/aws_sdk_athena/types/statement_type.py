"""Generated from Smithy shape ``com.amazonaws.athena#StatementType``."""

from typing import Literal, TypeAlias, cast

StatementType: TypeAlias = Literal[
    "DDL",
    "DML",
    "UTILITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatementType:
    return cast(StatementType, data)
