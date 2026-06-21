"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationSettingsStatusEnum``."""

from typing import Literal, TypeAlias, cast

ApplicationSettingsStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettingsStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationSettingsStatusEnum:
    return cast(ApplicationSettingsStatusEnum, data)
