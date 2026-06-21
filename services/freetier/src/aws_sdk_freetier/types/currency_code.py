"""Generated from Smithy shape ``com.amazonaws.freetier#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

CurrencyCode: TypeAlias = Literal["USD",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrencyCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CurrencyCode:
    return cast(CurrencyCode, data)
