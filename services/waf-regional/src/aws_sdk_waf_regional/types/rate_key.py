"""Generated from Smithy shape ``com.amazonaws.wafregional#RateKey``."""

from typing import Literal, TypeAlias, cast

RateKey: TypeAlias = Literal["IP",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RateKey:
    return cast(RateKey, data)
