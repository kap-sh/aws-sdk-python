"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessAuthType``."""

from typing import Literal, TypeAlias, cast

RedshiftServerlessAuthType: TypeAlias = Literal[
    "IAM",
    "USERNAME_PASSWORD",
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessAuthType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftServerlessAuthType:
    return cast(RedshiftServerlessAuthType, data)
