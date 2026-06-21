"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancySupportResultEnum``."""

from typing import Literal, TypeAlias, cast

DedicatedTenancySupportResultEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancySupportResultEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancySupportResultEnum:
    return cast(DedicatedTenancySupportResultEnum, data)
