"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftProvisionedAuthType``."""

from typing import Literal, TypeAlias, cast

RedshiftProvisionedAuthType: TypeAlias = Literal[
    "IAM",
    "USERNAME_PASSWORD",
    "USERNAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftProvisionedAuthType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftProvisionedAuthType:
    return cast(RedshiftProvisionedAuthType, data)
