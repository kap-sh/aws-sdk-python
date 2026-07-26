"""Generated from Smithy shape ``com.amazonaws.lightsail#Currency``."""

from typing import Literal, TypeAlias, cast

Currency: TypeAlias = Literal["USD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Currency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Currency:
    return cast(Currency, data)
