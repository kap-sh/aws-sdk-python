"""Generated from Smithy shape ``com.amazonaws.transfer#As2Transport``."""

from typing import Literal, TypeAlias, cast

As2Transport: TypeAlias = Literal["HTTP",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: As2Transport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> As2Transport:
    return cast(As2Transport, data)
