"""Generated from Smithy shape ``com.amazonaws.transfer#SetStatOption``."""

from typing import Literal, TypeAlias, cast

SetStatOption: TypeAlias = Literal[
    "DEFAULT",
    "ENABLE_NO_OP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetStatOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SetStatOption:
    return cast(SetStatOption, data)
