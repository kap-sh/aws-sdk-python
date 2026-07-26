"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Currency``."""

from typing import Literal, TypeAlias, cast

Currency: TypeAlias = Literal[
    "USD",
    "CNY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Currency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Currency:
    return cast(Currency, data)
