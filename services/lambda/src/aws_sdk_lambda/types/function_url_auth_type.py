"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionUrlAuthType``."""

from typing import Literal, TypeAlias, cast

FunctionUrlAuthType: TypeAlias = Literal[
    "NONE",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionUrlAuthType) -> str:
    return value


def deserialize_json(data: str) -> FunctionUrlAuthType:
    return cast(FunctionUrlAuthType, data)
