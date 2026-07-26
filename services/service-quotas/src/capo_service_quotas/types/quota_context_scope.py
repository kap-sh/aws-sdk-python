"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaContextScope``."""

from typing import Literal, TypeAlias, cast

QuotaContextScope: TypeAlias = Literal[
    "RESOURCE",
    "ACCOUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaContextScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuotaContextScope:
    return cast(QuotaContextScope, data)
