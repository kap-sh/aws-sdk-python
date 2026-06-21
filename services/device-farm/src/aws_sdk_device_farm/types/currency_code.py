"""Generated from Smithy shape ``com.amazonaws.devicefarm#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

CurrencyCode: TypeAlias = Literal["USD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CurrencyCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CurrencyCode:
    return cast(CurrencyCode, data)
