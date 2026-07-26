"""Generated from Smithy shape ``com.amazonaws.workspaces#SamlStatusEnum``."""

from typing import Literal, TypeAlias, cast

SamlStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SamlStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SamlStatusEnum:
    return cast(SamlStatusEnum, data)
